#!/bin/sh
set -e

while true; do
    ./venv/bin/python flask deploy
    if [[ "$?" == "0" ]]; then
        break
    fi
    echo Deploy command failed, retrying in 5 secs...
    sleep 5
done

exec "$@"
