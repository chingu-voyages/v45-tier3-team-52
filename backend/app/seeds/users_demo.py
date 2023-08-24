from app.models import db, User, environment, SCHEMA
from sqlalchemy import text


def seed_users():
    users = [{"first_name": "Jane", "last_name": "Doe",
              "email": "jane.doe@chin.com", "password": "password"}, {"first_name": "John", "last_name": "Doe",
                                                                      "email": "john.doe@chin.com", "password": "password1"}]

    db.session.add_all([User(**user)for user in users])
    db.session.commit()


def undo_users():
    if environment == "production":
        db.session.execute(
            f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))

    db.session.commit()
