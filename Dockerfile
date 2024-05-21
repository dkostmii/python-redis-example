FROM python:3.12.3-alpine3.19

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN adduser --disabled-password --no-create-home app-user

USER app-user
