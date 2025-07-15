from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.credit import CreditProfile

router = APIRouter(prefix="/credit", tags=["Credit"])

@router.get("/score")
def get_credit_score(user_id: int, db: Session = Depends(get_db)):
    profile = db.query(CreditProfile).filter(CreditProfile.user_id == user_id).first()
    if not profile:
        raise HTTPException(status_code=404, detail="Credit profile not found")
    return {"user_id": profile.user_id, "score": profile.score}


@router.get("/insight")
def get_credit_insight(user_id: int, db: Session = Depends(get_db)):
    profile = db.query(CreditProfile).filter(CreditProfile.user_id == user_id).first()
    if not profile:
        raise HTTPException(status_code=404, detail="Credit profile not found")

    return {
        "user_id": profile.user_id,
        "score": profile.score,
        "utilization": profile.utilization,
        "credit_age_months": profile.credit_age_months,
        "inquiries_last_6m": profile.inquiries_last_6m,
        "account_mix": profile.account_mix,
        "last_updated": profile.last_updated
    }
