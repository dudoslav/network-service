FROM python:3.10

WORKDIR /app

COPY ./main.py .
COPY ./requirements.txt .

RUN pip install -r requirements.txt

ENTRYPOINT hypercorn main:app --bind 0.0.0.0:8080