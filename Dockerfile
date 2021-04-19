FROM python:3.8-slim-buster
MAINTAINER Mike Vanbuskirk <mike@mikevanbuskirk.io>

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
