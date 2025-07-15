# app/services/prompts.py

predefined_prompts = [
    "How can I improve my credit score?",
    "What does credit utilization mean?",
    "How can I save more each month?",
    "Should I take a personal loan?",
    "What is the ideal credit mix?",
    "How do credit inquiries affect my score?",
    "Is it good to close old credit cards?",
    "How to manage debt wisely?",
]

def get_suggested_prompts():
    return predefined_prompts