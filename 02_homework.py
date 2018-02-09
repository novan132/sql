# INSERT

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    cars = [
            ('Honda', 'Civic', 3),
            ('Honda', 'Jazz', 2),
            ('Ford', 'Fiesta', 1),
            ('Ford', 'Focus', 1),
            ('Ford', 'Fusion', 2)
            ]
    try:
        c.executemany("INSERT INTO inventory VALUES(?, ?, ?)", cars)
    except sqlite3.OperationalError:
        print("oops. something wrong, try again ...")



