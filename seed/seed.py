import psycopg2
import os
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash
from datetime import datetime

load_dotenv()
conn = psycopg2.connect(
    database=os.getenv('DB_DATABASE'),
    user=os.getenv('DB_USERNAME'),
    password=os.getenv('DB_PASSWORD'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT')
)

cur = conn.cursor()

users = [{
    'username': f'user{i}',
    'email': f'user{i}@test.com',
    'full_name': f'first{i} last{i}',
    'password': f'!Test{i}'
} for i in range(1, 21)]

for user in users:
    hashed_password = generate_password_hash(user['password'])
    created_at = datetime.now()
    cur.execute(f'''
        INSERT
        INTO "user" (username, email, password, full_name, created_at)
        VALUES ('{user['username']}', '{user['email']}', '{hashed_password}', '{user['full_name']}', '{created_at}')
    ''')

conn.commit()

description_text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus vehicula sollicitudin nibh, ' \
                   'ac imperdiet leo laoreet quis. Duis risus ex, facilisis sed eros vitae, semper condimentum neque '
posts = [{
    'user_id': ((i+1) // 2),
    'image_url': f'static/{((i+1) // 2)}/{i}',
    'description': description_text
} for i in range(1, 21)]

for post in posts:
    created_at = datetime.now()
    cur.execute(f'''
        INSERT
        INTO post (user_id, image_url, description, created_at)
        VALUES ('{post['user_id']}', '{post['image_url']}', '{post['description']}', '{created_at}')
    ''')

conn.commit()
cur.close()
conn.close()
