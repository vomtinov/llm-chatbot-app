# 💬 LLM Chatbot App (FastAPI + OpenAI)

An elegant, minimal chatbot interface built using **FastAPI** and **Jinja templates**, powered by OpenAI’s GPT models. The project is fully containerized with Docker and ready to deploy on Azure App Service.

---

## 🚀 Features

- ⚡ FastAPI backend with HTML form interface
- 🧠 GPT-4o / GPT-3.5-turbo integration via OpenAI API
- 🐳 Dockerized for smooth containerization and deployment
- 🔐 Secure `.env`-based secret configuration
- ☁️ Azure App Service deployment ready
- 🧼 Minimal, readable code – perfect for learning or extending

---

## 🧰 Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/)
- [Jinja2](https://jinja.palletsprojects.com/)
- [OpenAI Python SDK](https://pypi.org/project/openai/)
- [Docker](https://www.docker.com/)
- [Azure App Service](https://learn.microsoft.com/en-us/azure/app-service/overview)

---

## 🛠️ Setup Locally

```bash
git clone https://github.com/vomtinov/llm-chatbot-app.git
cd llm-chatbot-app

# 1. Create .env file from template
cp .env.example .env

# 2. Paste your OpenAI API key in the .env file
# OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxx

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app locally
uvicorn app.main:app --reload --port 8000
```
## Run with Docker (Locally)

```bash
# Build the Docker image
docker build -t llm-chatbot-app .

# Run the container
docker run --rm -it --env-file .env -p 8000:8000 llm-chatbot-app
```
## Deploy to Azure App Service (Linux Container)

```bash
#Create Web App (Publish: Container, OS: Linux)

Use Docker Hub Image
→ manisuth/llm-chatbot-app:latest

Go to App Service → Configuration

Add Application Setting:
OPENAI_API_KEY = sk-xxxxxxxxxxxxxx

Restart the App

Access at:
https://<your-app-name>.azurewebsites.net/
```
## Security Best Practices

1. Secrets managed via .env or Azure App Settings

2. .env is excluded via .gitignore

3. Uses official openai library with timeouts and error handling

## project structure 
```bash
llm-chatbot-app/
├── app/
│   ├── main.py          # FastAPI entrypoint
│   ├── chatbot.py       # OpenAI logic
│   └── templates/
│       └── index.html   # Chat UI
├── requirements.txt
├── Dockerfile
├── .env.example
├── .gitignore
├── .dockerignore
└── README.md
```

# Made with 🤍 by Manish Suthar

