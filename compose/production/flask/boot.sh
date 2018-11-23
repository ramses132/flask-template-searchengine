#!/bin/sh

source ./venv/bin/activate
exec "$@"
while true; do
    ./venv/bin/python flask deploy
    if [[ "$?" == "0" ]]; then
        break
    fi
    echo "Deploy command failed, retrying in 5 secs..."
    sleep 5
done


exec ./venv/bin/python gunicorn -b :5000 --access-logfile - --error-logfile - search:app
