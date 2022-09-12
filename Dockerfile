FROM python:latest

WORKDIR /workspace

COPY ./requirements.txt .

RUN pip install -r requirements.txt