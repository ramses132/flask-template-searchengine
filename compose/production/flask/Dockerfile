FROM python:3.6-alpine
LABEL maintainer "Yugo <yugo132@gmail.com>"

RUN mkdir /app
COPY . /app
WORKDIR /app

RUN addgroup -S search
RUN adduser -S -G search search
RUN chown -R search /app
USER search

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
COPY compose/production/flask/run /run

ENV FLASK_ENV="docker"
EXPOSE 5000

ENTRYPOINT ["/run"]
