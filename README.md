# FastAPI + OpenAI (HTML UI)

Simple FastAPI app that serves an HTML form and calls OpenAI Chat Completions.

## Local (venv)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env   # add your OPENAI_API_KEY in .env
uvicorn app.main:app --reload --port 8000
