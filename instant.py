from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from openai import OpenAI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is running!"}

@app.get("/api", response_class=PlainTextResponse)
def idea():
    client = OpenAI()
    prompt = [
        {
            "role": "user",
            "content": "Come up with a new business idea for AI Agents"
        }
    ]
    response = client.chat.completions.create(
        model="gpt-5-nano",
        messages=prompt
    )
    return response.choices[0].message.content