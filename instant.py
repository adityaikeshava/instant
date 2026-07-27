from fastapi import FastAPI

app = FastAPI()

@app.get("/api", response_class=HTMLResponse)
def instant():
    message = "Live from production after deploying to vercel"
    client = OpenAI()
    messages = [{"role": "user", "content": message}]
    response = client.chat.completions.create(model="gpt-5-nano", messages=messages)
    reply = response.choices[0].message.content
    html = f"<html><head><title>Live in an Instant</title></head><body><h1>{reply}</h1></body></html>"
    return html