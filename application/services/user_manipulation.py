import sqlite3

from faker import Faker
import random


fake = Faker()


def create_new_user():
    with sqlite3.connect("phones.sqlite") as bd_con:
        cur = bd_con.cursor()
        cur.execute(
            """
            INSERT INTO phones(ContactName, PhoneValue)
            VALUES(:ContactName, :PhoneValue)
        """,
            (fake.name(), f"+38093{random.randint(1000000, 9999999)}"),
        )
        cur.execute("SELECT * FROM phones")
        result = cur.fetchall()
    return result


def delete_user(user_id: int):
    with sqlite3.connect("phones.sqlite") as bd:
        cur = bd.cursor()
        cur.execute(f"DELETE FROM phones WHERE PhoneId = {user_id}")
        cur.execute("SELECT * FROM phones")
        result = cur.fetchall()
        return result


def update_user(user_id: int):
    with sqlite3.connect("phones.sqlite") as bd_conn:
        cursor = bd_conn.cursor()
        cursor.execute(
            f"UPDATE phones SET ContactName='NOBODY' WHERE PhoneId LIKE '{user_id}%'"
        )
        cursor.execute("SELECT * FROM phones")
        result = cursor.fetchall()
        return result
