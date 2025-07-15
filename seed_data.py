from app.database import SessionLocal
from app.models.user import User
from app.models.credit import CreditProfile
from datetime import datetime, timezone

db = SessionLocal()

# Clean existing data
db.query(CreditProfile).delete()
db.query(User).delete()

# Add users
user1 = User(id=1, name="Alice", email="alice@example.com", hashed_password="hashedpassword1")
user2 = User(id=2, name="Bob", email="bob@example.com", hashed_password="hashedpassword2")
db.add_all([user1, user2])
db.commit()

# Add credit profiles
credit1 = CreditProfile(
    user_id=1,
    score=666,
    utilization=0.32,
    payment_history='{"2023-01": "on-time", "2023-02": "on-time", "2023-03": "late"}',
    credit_age_months=24,
    inquiries_last_6m=2,
    account_mix="credit_card,loan",
    last_updated=datetime.now(timezone.utc)

)
credit2 = CreditProfile(
    user_id=2,
    score=740,
    utilization=0.12,
    payment_history='{"2023-01": "on-time", "2023-02": "on-time", "2023-03": "on-time"}',
    credit_age_months=36,
    inquiries_last_6m=1,
    account_mix="credit_card,savings",
    last_updated=datetime.now(timezone.utc)
)
db.add_all([credit1, credit2])
db.commit()
db.close()

print("✅ Seeded mock users and credit profiles!")