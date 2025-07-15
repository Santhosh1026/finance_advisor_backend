# 💸 AI-Powered Personal Finance Advisor

A full-stack backend service built with FastAPI that provides personalized financial guidance based on users’ credit data and real-time AI analysis powered by **Ollama + Mistral**. Users can register securely, receive tailored insights into their credit behavior, and get intelligent advice to improve their financial standing.

---

## 📖 Project Overview

In many regions, individuals lack access to personalized, intelligent financial advice that understands their credit behavior and spending patterns. This project solves that by:

- Analyzing user credit scores and utilization
- Generating personalized recommendations with **LLMs (Large Language Models)**
- Ensuring secure and rule-bound user authentication
- Providing extensible architecture and seamless Docker deployment

---
## 🔍 Key Features

- 🔐 **Secure User Authentication** using JWT
- 💳 **Credit Score & Utilization API**
- 🧠 **AI-Generated Financial Advice** via Ollama (Mistral)
- 🧰 Modular architecture with clean business logic separation
- 🐳 **Dockerized** for portable and scalable deployment
- 📄 **Interactive Swagger Docs** available at `/docs`

---

## 📁 Project Structure

```
finance_advisor_backend/
│
├── app/
│ ├── main.py # FastAPI app entry
│ ├── config.py # .env loader
│ ├── database.py # SQLAlchemy DB setup
│
│ ├── models/ # SQLAlchemy ORM Models
│ │ ├── user.py
│ │ ├── credit.py
│ │ └── transaction.py
│
│ ├── schemas/ # Pydantic request/response models
│ │ ├── user.py
│ │ ├── credit.py
│ │ └── transaction.py
│
│ ├── routers/ # API endpoints (controllers)
│ │ ├── auth.py
│ │ ├── credit.py
│ │ ├── advice.py
│
│ ├── services/ # Business logic layer
│ │ ├── auth_service.py
│ │ ├── credit_analyzer.py
│ │ └── ollama_service.py
│
│ ├── auth/ # Auth-specific helpers
│ │ ├── jwt_handler.py
│ │ └── hash.py
│
├── init_db.py # DB init script
├── seed_data.py # Mock user & credit profile seeder
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── database.sqlite # SQLite for local DB
├── .env # Environment variables
├── README.md
```
## Required packages:

```fastapi

uvicorn

sqlalchemy

pydantic[email]

python-jose

passlib[bcrypt]

requests

python-dotenv
```


# 1. Create and activate virtual environment
```
python -m venv venv
source venv/bin/activate      # Linux / macOS
venv\Scripts\activate         # Windows
```

# 2. Install dependencies
```
pip install -r requirements.txt
```

# 3. Initialize DB and seed sample data
```
python init_db.py
python seed_data.py
```
# 4. Run backend server
```
uvicorn app.main:app --reload
```
## Ollama Installation
```
curl -fsSL https://ollama.com/install.sh | sh
ollama pull mistral
ollama serve
```
## Example Prompt
User Credit Details:
Score: 720
Utilization: 0.35
Credit Age: 18 months
Inquiries Last 6M: 1
Account Mix: credit_card, loan

Based on this, give personalized financial advice in 3 bullet points.

## 🐳 Docker Deployment
```
docker build -t finance-backend .
```
## Run the Container
```
docker run -d -p 8000:8000 finance-backend
```
## 🧪 API Reference (Swagger Docs)
| Endpoint          | Method | Description                          |
| ----------------- | ------ | ------------------------------------ |
| `/auth/register`  | POST   | Register a new user                  |
| `/auth/login`     | POST   | Login and get JWT token              |
| `/credit/score`   | GET    | Get the user's credit score          |
| `/credit/insight` | GET    | Get credit usage & behavior insights |
| `/ai/advice`      | GET    | Get personalized financial advice    |
| `/ai/prompts`     | GET    | Get predefined AI prompts            |

## 🧠 Predefined Prompts (Examples)
“How do I reduce credit utilization?”

“Tips to improve credit score quickly”

“Is it safe to take a personal loan with high credit utilization?”

## 📌 Notes
SQLite used for development (can be swapped for PostgreSQL/MySQL)

Ollama must be running for AI endpoint to work

Mistral model requires ~4GB+ RAM

---

## ⚙️ Requirements

Install with:

```bash
pip install -r requirements.txt
```


## Thank You

