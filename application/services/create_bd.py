import sqlite3


def bd_creator() -> None:
    """
    Функция для создания и минимальной работы с БД
    :return: данные из БД [[значение где phone_value>200], первое значение]
    """
    with sqlite3.connect("phones.sqlite") as bd_connection:
        cursor = bd_connection.cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS phones(
                 PhoneId INTEGER PRIMARY KEY AUTOINCREMENT,
                 ContactName TEXT,
                 PhoneValue INTEGER
            )
        """
        )
    return None
