import psycopg2
import os
from dotenv import load_dotenv
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


load_dotenv()
conn = psycopg2.connect(
    database=os.getenv("postgres"),
    user=os.getenv("DB_USERNAME"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
)

conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

cur = conn.cursor()

cur.execute(
    """
    DROP DATABASE IF EXISTS soengram;
"""
)

cur.execute(
    """
    CREATE DATABASE soengram;
"""
)

conn.commit()
cur.close()
conn.close()
