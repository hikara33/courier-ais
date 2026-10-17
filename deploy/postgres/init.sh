#!/bin/bash
# Выполняется один раз при первом создании БД. Одна БД, четыре схемы, у каждой свой пользователь.
set -e
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE EXTENSION IF NOT EXISTS postgis;

    CREATE ROLE core_user     LOGIN PASSWORD '${CORE_DB_PASSWORD}';
    CREATE ROLE dispatch_user LOGIN PASSWORD '${DISPATCH_DB_PASSWORD}';
    CREATE ROLE tracking_user LOGIN PASSWORD '${TRACKING_DB_PASSWORD}';
    CREATE ROLE notify_user   LOGIN PASSWORD '${NOTIFY_DB_PASSWORD}';

    CREATE SCHEMA core     AUTHORIZATION core_user;
    CREATE SCHEMA dispatch AUTHORIZATION dispatch_user;
    CREATE SCHEMA tracking AUTHORIZATION tracking_user;
    CREATE SCHEMA notify   AUTHORIZATION notify_user;

    ALTER ROLE core_user     SET search_path = core, public;
    ALTER ROLE dispatch_user SET search_path = dispatch, public;
    ALTER ROLE tracking_user SET search_path = tracking, public;
    ALTER ROLE notify_user   SET search_path = notify, public;
EOSQL
