FROM python:3.10-slim-buster
LABEL authors="max-coder"

WORKDIR /app
COPY . /app

RUN apt-get update

RUN pip install -r requirements.txt
RUN rm -rf /var/lib/apt/lists/*

CMD ["python", "main.py"]