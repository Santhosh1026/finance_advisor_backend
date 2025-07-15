from ollama import Client

def generate_credit_insight(credit_data: dict) -> str:
    client = Client(host='http://localhost:11434')

    prompt = f"""
    A user's credit profile looks like this:

    - Credit Score: {credit_data['score']}
    - Credit Utilization: {credit_data['utilization_score']}%
    - Credit Age: {credit_data['credit_age']} months
    - Inquiries (last 6 months): {credit_data['inquiries']}
    - Account Mix: {credit_data['mix']}
    - Payment Score: {credit_data['payment_score']}

    Based on this, provide helpful personalized advice on how to improve their credit score.
    """

    response = client.chat(
        model="mistral",  # or deepseek-coder if installed
        messages=[{"role": "user", "content": prompt}]
    )

    return response['message']['content']