FROM postgres:13

COPY db.sql /docker-entrypoint-initdb.d/db.sql
COPY schema.sql /docker-entrypoint-initdb.d/schema.sql