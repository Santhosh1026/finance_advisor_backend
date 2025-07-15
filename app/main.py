from fastapi import FastAPI
from app.routers import credit, advice, auth  # <-- add auth

app = FastAPI(
    title="AI Personal Finance Advisor",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"message": "Backend is running 🚀"}

app.include_router(credit.router)
app.include_router(advice.router)
app.include_router(auth.router)