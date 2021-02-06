import psycopg2

conn = psycopg2.connect(
    database="soengram",
    user="postgres",
    password="admin",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

cur.execute('''
            CREATE TABLE "user" (
                user_id SERIAL PRIMARY KEY,
                email VARCHAR(255) UNIQUE NOT NULL,
                username VARCHAR(255) UNIQUE NOT NULL,
                full_name VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL,
                created_at TIMESTAMP
            );
            ''')

conn.commit()
conn.close()
