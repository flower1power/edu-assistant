from fastapi import FastAPI, Form, HTTPException
from fastapi.responses import FileResponse
from openai import OpenAIError

from edu_assistant.assistant import create_response
from edu_assistant.config import RoleType, TemplateType

app = FastAPI()


@app.get('/demo')
def demo():
    return FileResponse("templates/demo.html")


@app.post('/ask')
def ask(
        role: RoleType = Form(description="Role of AI assistant"),
        template: TemplateType = Form(description="Response format"),
        question: str = Form(description="Student question", examples=["Ты кто?"]),
) -> str:
    """Ask question to educational assistant."""
    try:
        return create_response(
            llm_key="ollama",
            role=role,
            template=template,
            prompt=question
        )
    except OpenAIError as error:
        raise HTTPException(status_code=502, detail=str(error)) from error
