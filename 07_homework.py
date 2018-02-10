# SELECT count()

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    sql = {
            'Civic': "SELECT count(make) FROM orders WHERE model = 'Civic'",
            'Jazz': "SELECT count(make) FROM orders WHERE model = 'Jazz'",
            'Focus': "SELECT count(make) FROM orders WHERE model = 'Focus'",
            'Fusion': "SELECT count(make) FROM orders WHERE model = 'Fusion'",
            'Fiesta': "SELECT count(make) FROM orders WHERE model = 'Fiesta'"
    }

    try:
        for key, value in sql.items():
            c.execute(value)

            result = c.fetchone()

            print(key + ":" , result[0])

    except sqlite3.OperationalError:
        print("oops. something wrong. try again ...")