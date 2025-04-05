from fastapi import FastAPI
from pydantic import BaseModel
import ollama
from fastapi.middleware.cors import CORSMiddleware
import re  # Import regex module

app = FastAPI()

# Enable CORS for frontend on port 3000
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat_endpoint(req: ChatRequest):
    response = ollama.chat(
        model="deepseek-r1:7b",  # ✅ Ensure correct model name
        messages=[{"role": "user", "content": req.message}]
    )

    # Extract reply from the response
    reply = response.get("message", {}).get("content", "").strip()

    # Remove <think> </think> tags and unnecessary placeholders
    reply = re.sub(r"<think>\s*</think>", "", reply).strip()  # Remove <think> </think>
    
    unwanted_phrases = ["thinking...", "hmm...", "let me see..."]
    for phrase in unwanted_phrases:
        reply = reply.replace(phrase, "").strip()

    return {"reply": reply}
