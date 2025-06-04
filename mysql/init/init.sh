#!/bin/bash
set -e

echo "Running database initialization..."

# Tunggu hingga MySQL benar-benar siap
while ! mysqladmin ping -h"localhost" -u"root" -p"$MYSQL_ROOT_PASSWORD" --silent; do
    sleep 1
done

# Jalankan skrip SQL
mysql -u root -p"$MYSQL_ROOT_PASSWORD" "$MYSQL_DATABASE" < /docker-entrypoint-initdb.d/sql.init

echo "Initialization complete."