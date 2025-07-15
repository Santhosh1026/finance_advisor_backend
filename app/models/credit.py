from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class CreditProfile(Base):
    __tablename__ = "credit_profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)
    score = Column(Integer, nullable=False)
    utilization = Column(Float, nullable=False)
    payment_history = Column(String, nullable=True)  # Could store as JSON or delimited string
    credit_age_months = Column(Integer, nullable=False)
    inquiries_last_6m = Column(Integer, nullable=False)
    account_mix = Column(String, nullable=True)
    last_updated = Column(DateTime, default=datetime.utcnow)

    # Define relationship back to the User
    user = relationship("app.models.user.User", back_populates="credit_profile")
