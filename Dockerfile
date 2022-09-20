FROM python:3.10

WORKDIR /app

# Copy and install requirements
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy app
COPY ./main.py .

# Serve app
ENTRYPOINT hypercorn main:app --bind 0.0.0.0:8080