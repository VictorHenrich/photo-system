FROM python:3.12-slim

WORKDIR /app

COPY . /app

RUN apt-get update && \
    apt-get install -y git && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r /app/requirements.txt

CMD ["python3", "run_api.py"]
