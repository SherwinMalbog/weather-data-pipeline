"""
Connection helper for the warehouse (Postgres standing in for
Redshift/Synapse/BigQuery -- see docs/03-Cloud-Service-Equivalents.md).
"""

import os

import psycopg2
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    return psycopg2.connect(
        host=os.environ.get("WAREHOUSE_HOST", "localhost"),
        port=os.environ.get("WAREHOUSE_PORT", "5432"),
        dbname=os.environ.get("WAREHOUSE_DB", "warehouse"),
        user=os.environ.get("WAREHOUSE_USER", "warehouse"),
        password=os.environ.get("WAREHOUSE_PASSWORD", "warehouse"),
    )
