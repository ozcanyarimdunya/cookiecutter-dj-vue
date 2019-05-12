#!/usr/bin/env bash

cmd="$@"

function postgres_ready(){
python << END
import sys
import psycopg2
import os

try:
    host = os.getenv('POSTGRES_HOST')
    dbname = os.getenv('POSTGRES_DB')
    user = os.getenv('POSTGRES_USER')
    password = os.getenv('POSTGRES_PASSWORD')
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=5432)
except psycopg2.OperationalError:
    sys.exit(-1)
sys.exit(0)
END
}

until postgres_ready; do
  >&2 echo "... Sleeping. Postgres is unavailable"
  sleep 1
done

>&2 echo "... Continuing. Postgres is up"
exec $cmd