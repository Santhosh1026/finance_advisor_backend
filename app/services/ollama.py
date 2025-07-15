# app/services/ollama.py

import requests

def generate_ai_response(prompt: str) -> str:
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "mistral", "prompt": prompt, "stream": False},
            timeout=30
        )
        response.raise_for_status()
        return response.json().get("response", "⚠️ No reply generated.")
    except Exception as e:
        return f"⚠️ Error: {str(e)}"