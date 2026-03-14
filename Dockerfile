FROM python:3.11-slim

WORKDIR /app

# Встановлюємо Jinja2
RUN pip install jinja2

COPY . .

# Відкриваємо порт
EXPOSE 3000

CMD ["python", "main.py"]