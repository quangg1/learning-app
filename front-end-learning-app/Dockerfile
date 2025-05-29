FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV API_BE=learning-app
ENV DOMAIN_BE=https://learning-app-backend-0gfg.onrender.com
ENV SENTIMENT_API_DOMAIN=''
ENV TURN_ON_SCREEN=False

EXPOSE 8080

CMD ["flet", "run", "--port", "8080", "--host", "0.0.0.0", "main.py"] 