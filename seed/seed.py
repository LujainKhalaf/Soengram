import psycopg2
import os
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash
from datetime import datetime

load_dotenv()
conn = psycopg2.connect(
    database=os.getenv("DB_DATABASE"),
    user=os.getenv("DB_USERNAME"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
)

cur = conn.cursor()

folder_dir = os.getenv("POST_UPLOAD_FOLDER") or "" + "seed/"
description_text = (
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus vehicula sollicitudin nibh, "
    "ac imperdiet leo laoreet quis. Duis risus ex, facilisis sed eros vitae, semper condimentum neque "
)

users = [
    {
        "username": f"user{i}",
        "email": f"user{i}@test.com",
        "full_name": f"first{i} last{i}",
        "password": f"!Test{i}",
    }
    for i in range(1, 21)
]

for index, user in enumerate(users):
    hashed_password = generate_password_hash(user["password"])
    created_at = datetime.now()
    cur.execute(
        f"""
        INSERT
        INTO "user" (username, email, password, full_name, created_at)
        VALUES ('{user['username']}', '{user['email']}', '{hashed_password}', '{user['full_name']}', '{created_at}')
    """
    )

conn.commit()

user1_posts = [
    {"user_id": 1, "image_url": f"{folder_dir}{i}.jpg", "description": description_text}
    for i in range(2, 14)
]

for post in user1_posts:
    created_at = datetime.now()
    cur.execute(
        f"""
        INSERT
        INTO post (user_id, image_url, description, created_at)
        VALUES ('{post['user_id']}', '{post['image_url']}', '{post['description']}', '{created_at}')
    """
    )

other_user_posts = [
    {"user_id": i, "image_url": f"{folder_dir}1.jpg", "description": description_text}
    for i in range(2, 21)
]

for post in other_user_posts:
    created_at = datetime.now()
    cur.execute(
        f"""
        INSERT
        INTO post (user_id, image_url, description, created_at)
        VALUES ('{post['user_id']}', '{post['image_url']}', '{post['description']}', '{created_at}')
    """
    )

for index in range(1, 21):
    posts = [
        {
            "user_id": index,
            "image_url": f"{folder_dir}1.jpg",
            "description": description_text,
        }
        for i in range(1, 21)
    ]

    for post in posts:
        created_at = datetime.now()
        cur.execute(
            f"""
            INSERT
            INTO post (user_id, image_url, description, created_at)
            VALUES ('{post['user_id']}', '{post['image_url']}', '{post['description']}', '{created_at}')
        """
        )

for index in range(1, 11):
    following_ids = range(11, 21)

    for following_id in following_ids:
        cur.execute(
            f"""
            INSERT
            INTO followers (user_id, following_id)
            VALUES ('{index}', '{following_id}')
        """
        )

conn.commit()
cur.close()
conn.close()
