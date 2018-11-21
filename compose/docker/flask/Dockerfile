FROM python:3.6-alpine

COPY . /app
WORKDIR /app

RUN addgroup -S search
RUN adduser -S -G search search
RUN chown -R search /app
USER search

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt

COPY compose/production/flask/run /run
ENTRYPOINT ["/run"]
