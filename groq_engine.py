from groq import Groq
from config import GROQ_API_KEY, MODEL_NAME

client = Groq(api_key=GROQ_API_KEY)

def ask_question(query: str, history=None) -> str:
    if not isinstance(query, str):
        query = str(query)

    if history is None:
        history = []

    messages = [
        {
            "role": "system",
            "content": (
                "You are a helpful school assistant based in Lucknow, India. "
                "Always answer concisely (1–2 lines max) and assume Indian time (IST), currency (INR), and culture. "
                "If user asks for local details, assume they are referring to Lucknow unless specified otherwise."
            ),
        },
        *history,
        {
            "role": "user",
            "content": query,
        },
    ]

    print("📡 Sending query to Groq...")

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        temperature=0.7,
        max_tokens=150,
        top_p=1,
        stream=False,
    )

    return response.choices[0].message.content.strip()
