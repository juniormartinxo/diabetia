FROM python:3.11.14-slim-bookworm

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends bash tzdata ca-certificates \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
    && python -m playwright install --with-deps \
    && rm -rf /var/lib/apt/lists/*

COPY . .

CMD ["python", "main.py"]
