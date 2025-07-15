from pydantic import BaseModel, EmailStr, Field, validator
import re

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str = Field(min_length=8, max_length=16)

    @validator("password")
    def validate_password(cls, v, values):
        name = values.get("name", "")
        email = values.get("email", "")
        if name.lower() in v.lower() or email.lower() in v.lower():
            raise ValueError("Password should not contain your name or email")
        if not re.search(r'[A-Z]', v) or not re.search(r'[a-z]', v) or not re.search(r'\d', v) or not re.search(r'[@$!%*#?&]', v):
            raise ValueError("Password must include upper, lower, digit and special character")
        return v

class UserLogin(BaseModel):
    email: EmailStr
    password: str
