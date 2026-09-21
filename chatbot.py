from openai import OpenAI
from config import GROQ_API_KEY, MODEL

client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)

question = input("Ask the chatbot: ")

response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {
            "role": "system",
            "content": "You are a general student expense chatbot. You do not have access to the student's private expense data."
        },
        {
            "role": "user",
            "content": question
        }
    ]
)

print("\nChatbot:")
print(response.choices[0].message.content)