from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.credit import CreditProfile
from app.services.insight_service import generate_credit_insight

router = APIRouter()

@router.get("/credit/insight")
def get_credit_insight(user_id: int):
    db: Session = SessionLocal()
    profile = db.query(CreditProfile).filter(CreditProfile.user_id == user_id).first()

    if not profile:
        raise HTTPException(status_code=404, detail="User not found")

    credit_data = {
        "score": profile.score,
        "utilization_score": int(profile.utilization * 100),
        "credit_age": profile.credit_age_months,
        "inquiries": profile.inquiries_last_6m,
        "mix": profile.account_mix,
        "payment_score": 0 if "late" in list(profile.payment_history.values()) else 100
    }

    try:
        insight = generate_credit_insight(credit_data)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI generation failed: {str(e)}")

    return {"user_id": user_id, "insight": insight}