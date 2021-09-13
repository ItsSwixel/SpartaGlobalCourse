import sqlite3
from contextlib import closing


def create_table():
    with closing(sqlite3.connect("data.db")) as connection:
        with closing(connection.cursor()) as cursor:
            cursor.execute("CREATE TABLE operations_table (id INTEGER PRIMARY KEY, name TEXT);")
            connection.commit()


def insert():
    with closing(sqlite3.connect("data.db")) as connection:
        with closing(connection.cursor()) as cursor:
            cursor.execute("INSERT INTO operations_table (name) VALUES ('addition');")
            connection.commit()


def show():
    with closing(sqlite3.connect("data.db")) as connection:
        with closing(connection.cursor()) as cursor:
            cursor.execute("SELECT * FROM operations_table;")
            records = cursor.fetchall()
            print(records)
