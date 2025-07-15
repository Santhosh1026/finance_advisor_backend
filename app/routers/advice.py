from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.credit import CreditProfile
import requests

router = APIRouter(prefix="/ai", tags=["AI Advice"])

OLLAMA_API_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "mistral"

# ✅ Predefined finance prompt suggestions
predefined_prompts = [
    "How can I improve my credit score?",
    "What does credit utilization mean?",
    "How to reduce my loan burden?",
    "How can I save more each month?",
    "What is a healthy account mix?",
    "What is a good credit age?"
]

def is_finance_related(message: str) -> bool:
    keywords = ["credit", "loan", "score", "utilization", "debt", "saving", "bank", "investment", "finance", "budget"]
    return any(word in message.lower() for word in keywords)

@router.get("/prompts")
def get_predefined_prompts():
    return {"prompts": predefined_prompts}

# ✅ Chatbot style advice: user sends a free-form question
@router.get("/advice")
def get_chat_advice(user_id: int, question: str = Query(...), db: Session = Depends(get_db)):
    if not is_finance_related(question):
        return {
            "response": "❌ Sorry, this assistant only responds to finance-related questions."
        }

    profile = db.query(CreditProfile).filter(CreditProfile.user_id == user_id).first()
    if not profile:
        raise HTTPException(status_code=404, detail="Credit profile not found")

    prompt = (
        f"You are a financial advisor. Based on the user's credit profile:\n"
        f"Score: {profile.score}, Utilization: {profile.utilization}, "
        f"Credit Age: {profile.credit_age_months} months, "
        f"Inquiries: {profile.inquiries_last_6m}, Account Mix: {profile.account_mix}\n\n"
        f"The user asks: \"{question}\"\n"
        f"Provide a professional, simple answer for the user."
    )

    try:
        response = requests.post(OLLAMA_API_URL, json={
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False
        })
        response.raise_for_status()
        result = response.json()
        return {"response": result.get("response", "⚠️ No response received.")}
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Ollama error: {str(e)}")
