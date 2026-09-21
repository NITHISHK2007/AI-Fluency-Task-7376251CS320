from openai import OpenAI
from config import GROQ_API_KEY, MODEL
from tools import get_student_data, get_total_expenses, get_balance

client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)

question = input("Ask the AI Agent: ")

data = get_student_data()
total = get_total_expenses()
balance = get_balance()

response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {
            "role": "system",
            "content": f"""
You are a student expense AI agent.

You have access to private student expense data through tools.

Student data:
Monthly allowance: ₹{data["monthly_allowance"]}
Food: ₹{data["food"]}
Travel: ₹{data["travel"]}
Study materials: ₹{data["study_materials"]}
Other: ₹{data["other"]}
Total expenses: ₹{total}
Remaining balance: ₹{balance}

Answer the user's question using this data.
Keep the answer simple and clear.
"""
        },
        {
            "role": "user",
            "content": question
        }
    ]
)

print("\nAI Agent:")
print(response.choices[0].message.content)