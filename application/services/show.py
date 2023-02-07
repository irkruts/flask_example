import sqlite3


def show_all_items():
    with sqlite3.connect("phones.sqlite") as bd_con:
        cursor = bd_con.cursor()
        cursor.execute("SELECT * FROM phones")
        result = cursor.fetchall()
        return result


def show_some_from_bd(user_id):
    with sqlite3.connect("phones.sqlite") as bd_con:
        cursor = bd_con.cursor()
        cursor.execute(f"SELECT * FROM phones WHERE PhoneId > {user_id}")
        result = cursor.fetchall()
        return result
