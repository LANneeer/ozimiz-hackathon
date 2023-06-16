FROM python:3.10

WORKDIR /app

# environment
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1
ENV PYTHONBUFFERED 1
ENV POSTGRES_DB=hackathon
ENV POSTGRES_USER=ozimiz
ENV POSTGRES_PASSWORD=123
ENV POSTGRES_HOST=127.0.0.1
ENV POSTGRES_PORT=5432

COPY . .

RUN apt-get update && \
    apt-get install nginx vim -y --no-install-recommends