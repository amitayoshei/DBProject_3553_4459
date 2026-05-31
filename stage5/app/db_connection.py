"""
db_connection.py
Handles the database connection for the PowerGym Pro application.
Uses psycopg2 with python-dotenv to load credentials from .env file.
"""

import psycopg2
import os
from pathlib import Path
from dotenv import load_dotenv


def get_connection():
    """
    Establish and return a psycopg2 connection to the Supabase PostgreSQL database.
    Loads credentials from the .env file located in the workspace root.
    """
    # Walk up from this file's location to find the .env
    base_dir = Path(__file__).resolve().parent.parent.parent
    env_path = base_dir / ".env"
    load_dotenv(dotenv_path=env_path)

    host = os.getenv("DB_HOST")
    dbname = os.getenv("DB_NAME")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    port = os.getenv("DB_PORT", "5432")

    conn = psycopg2.connect(
        host=host,
        dbname=dbname,
        user=user,
        password=password,
        port=port,
        sslmode="require",
        connect_timeout=10,
    )
    return conn
