import os
from openai import OpenAI

_client = None
def _client_instance():
    global _client
    if _client is None:
        _client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    return _client

def ask_llm(prompt: str) -> str:
    if not os.getenv("OPENAI_API_KEY"):
        return f"(no key) Echo: {prompt}"
    try:
        resp = _client_instance().chat.completions.create(
            model=os.getenv("OPENAI_MODEL", "gpt-3.5-turbo"),
            messages=[{"role":"user","content":prompt}]
        )
        return resp.choices[0].message.content
    except Exception as e:
        return f"(error) {e}"
