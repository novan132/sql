# homework

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    try:
        c.execute("CREATE TABLE inventory (Make TEXT, Model TEXT, Quantity INT )")
    except sqlite3.OperationalError:
        print("oops. something wrong. try again ...")
