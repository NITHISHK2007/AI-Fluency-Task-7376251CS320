import os
from dotenv import load_dotenv

load_dotenv()

PROVIDER = os.getenv("PROVIDER")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL = os.getenv("MODEL")

STUDENT_DATA = {
    "monthly_allowance": 5000,
    "food": 2000,
    "travel": 800,
    "study_materials": 700,
    "other": 300
}