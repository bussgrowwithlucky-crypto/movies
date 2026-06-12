FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

COPY . /app/

RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 8080

CMD ["python", "bot.py"]
