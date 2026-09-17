-- Runs once, automatically, the first time the postgres container starts
-- (mounted into /docker-entrypoint-initdb.d/).

-- Airflow needs its own metadata database, separate from the warehouse.
CREATE DATABASE airflow;

-- Warehouse schemas: raw (landed data), staging (cleaned by dbt),
-- marts (business-ready tables, also built by dbt).
CREATE SCHEMA IF NOT EXISTS raw;
CREATE SCHEMA IF NOT EXISTS staging;
CREATE SCHEMA IF NOT EXISTS marts;
