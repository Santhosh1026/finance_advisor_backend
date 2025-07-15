from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserLogin
from app.services.auth_service import register_user, authenticate_user
from app.database import get_db

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register")
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    user = register_user(db, user_data)
    return {"message": "User registered successfully", "user_id": user.id}

@router.post("/login")
def login(user_data: UserLogin, db: Session = Depends(get_db)):
    token = authenticate_user(db, user_data.email, user_data.password)
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    return {"access_token": token, "token_type": "bearer"}