FROM python:3.9.9-alpine
MAINTAINER prapeller

ENV PYTHONUNBUFFERED 1

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /core
WORKDIR /core
COPY ./core /core
RUN adduser -D app_daemon
USER app_daemon
