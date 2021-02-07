import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()
conn = psycopg2.connect(
    database=os.getenv('DB_DATABASE'),
    user=os.getenv('DB_USERNAME'),
    password=os.getenv('DB_PASSWORD'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT')
)

cur = conn.cursor()

cur.execute('''
            CREATE TABLE "user" (
                user_id SERIAL PRIMARY KEY,
                email VARCHAR(50) UNIQUE NOT NULL,
                username VARCHAR(20) UNIQUE NOT NULL,
                full_name VARCHAR(50) NOT NULL,
                password VARCHAR(255) NOT NULL,
                created_at TIMESTAMP
            );
            ''')
conn.commit()
conn.close()
