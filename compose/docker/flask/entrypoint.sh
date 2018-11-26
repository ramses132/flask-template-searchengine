#!/bin/sh
set -e

postgres_connection() {
python << END
import sys
import psycopg2

try:
    psycopg2.connect(
        dbname="${POSTGRES_DB}",
        user="${POSTGRES_USER}",
        password="${POSTGRES_PASSWORD}",
        host="postgres"
    )
except psycopg2.OperationalError:
    sys.exit(-1)
sys.exit(0)
END
}

if [[  -z "$POSTGRES_DB" ]]; then
    echo "Running without postgres enviroment..."
else
    export LOCAL_DATABASE_URL="postgres://${POSTGRES_USER}:${POSTGRES_PASSWORD}@postgres:5432/${POSTGRES_DB}"
    export TEST_DATABASE_URL="postgres://${POSTGRES_USER}:${POSTGRES_PASSWORD}@postgres:5432/${POSTGRES_DB}"
    while ! [[ postgres_connection ]]; do
        >&2 echo Postgres connection failed, retrying in 5 secs...
        sleep 5
    done
fi

while true; do
    flask deploy
    if [[ "$?" == "0" ]]; then
        break
    fi
    echo Deploy command failed, retrying in 5 secs...
    sleep 5
done

exec "$@"
