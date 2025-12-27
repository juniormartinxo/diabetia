FROM python:3.11.14-alpine3.23

WORKDIR /app

RUN apk add --no-cache tzdata bash

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]
