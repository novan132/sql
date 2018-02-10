import sqlite3
import random

with sqlite3.connect("newnum.db") as connection:
    c = connection.cursor()
    try:
        c.execute("DROP TABLE IF EXISTS numbers")
        c.execute("CREATE TABLE numbers (num INT)")

        for i in range(100):
            c.execute("INSERT INTO numbers VALUES (?)", (random.randint(0, 100),))
    except sqlite3.OperationalError:
        print("oops. something wrong. try again")

