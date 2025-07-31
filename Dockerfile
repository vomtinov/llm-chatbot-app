FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose the port; Azure sets $PORT, we default to 8000
EXPOSE 8000

# CMD uses ${PORT:-8000} so it works locally and on Azure
CMD ["sh","-c","uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]
