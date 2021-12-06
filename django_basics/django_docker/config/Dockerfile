FROM python:3.9-alpine3.14
MAINTAINER prapeller
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /django_docker
COPY . /django_docker/

RUN pip install --upgrade pip && pip install -r requirements.txt
