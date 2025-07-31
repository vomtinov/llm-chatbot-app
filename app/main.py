import os
from pathlib import Path
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
from .chatbot import ask_llm

# load .env locally
load_dotenv()

app = FastAPI()
# point Jinja to the templates folder inside the app package
templates = Jinja2Templates(directory=Path(__file__).parent / "templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "response": ""})

@app.post("/ask", response_class=HTMLResponse)
async def ask(request: Request, message: str = Form(...)):
    reply = ask_llm(message)
    return templates.TemplateResponse("index.html", {"request": request, "response": reply})

@app.get("/health")
async def health():
    return {"status":"ok"}
