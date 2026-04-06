from dotenv import load_dotenv
from fastapi.testclient import TestClient

from edu_assistant.api import app

load_dotenv()

client = TestClient(app)

response = client.post(
    "/ask",
    data={
        "role": "math_tutor",
        "template": "tutor_quick_answer",
        "question": "Что такое число Пи?",
    })

print(response.text)
