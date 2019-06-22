#!/bin/sh
# wait-for-mysql.sh

set -e

host="$1"
shift
cmd="$@"

until mysqladmin -h "$host" -u "mergulhando" -pchangeme ping; do
  >&2 echo "Mysql is unavailable - sleeping"
  sleep 5
done

>&2 echo "Mysql is up and running - calling Flask Startup"
exec $cmd