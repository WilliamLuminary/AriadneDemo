FROM python:3.11
LABEL authors="william"
LABEL version="1.0"
LABEL description="AriadneDemo Python application in Docker"

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt


CMD ["python", "app.py"]
