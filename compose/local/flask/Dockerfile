FROM python:3.6-alpine
LABEL maintainer "Yugo <yugo132@gmail.com>"

COPY . /app
WORKDIR /app

RUN addgroup -S search
RUN adduser -S -G search search
RUN chown -R search /app
USER search

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

COPY requirements.txt requirements.txt
RUN python -m venv venv && pip install --upgrade pip && venv/bin/pip install -r requirements.txt


COPY app app
COPY migrations migrations
COPY search.py search.py
COPY config.py config.py 

EXPOSE 5000
COPY compose/local/flask/boot /boot
ENTRYPOINT ["/boot"]
