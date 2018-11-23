FROM python:3.6-alpine
LABEL maintainer "Yugo <yugo132@gmail.com>"


WORKDIR /app

COPY . /app

RUN addgroup -S search
RUN adduser -S -G search search


RUN apk update && \
    apk add libpq postgresql-dev gcc python3-dev musl-dev build-base

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip && \
    pip install -r requirements.txt


COPY app ./
COPY migrations ./
COPY search.py ./
COPY config.py ./ 

COPY compose/production/flask/boot.sh ./boot.sh
RUN chown search ./boot.sh
RUN chmod a+x ./boot.sh
RUN chown -R search ./

USER search

EXPOSE 5000

ENTRYPOINT ["./boot.sh"]
