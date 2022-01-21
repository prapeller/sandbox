FROM python:3.10-alpine
MAINTAINER prapeller

ENV PYTHONUNBUFFERED 1

COPY requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt
RUN pip install gunicorn
RUN apk del .tmp-build-deps

WORKDIR /todolist
COPY ./todolist /todolist
RUN sed -i 's/force_text/force_str/g' /usr/local/lib/python3.10/site-packages/graphene_django/utils/utils.py

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static
#RUN adduser -D app_daemon
#RUN chown -R app_daemon /vol/
#RUN chown -R 755 /vol/web
#USER app_daemon
