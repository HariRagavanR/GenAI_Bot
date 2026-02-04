import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

print("🤖 Groq GenAI Chatbot Ready (type 'exit' to quit)")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Bye machi 👋")
        break

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are a strict AI tutor. Definition rules: 1) GenAI always means Generative AI. 2) Never expand GenAI as General AI or AGI. 3) If user asks about GenAI, explain only Generative AI. 4) Keep answers factual, simple, and beginner-friendly. If confused, correct yourself immediately."},
            {"role": "user", "content": user_input}
        ]
    )

    print("Bot:", response.choices[0].message.content)
