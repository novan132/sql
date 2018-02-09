# INSERT 

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    try:
        c.execute("CREATE TABLE orders (make TEXT, model TEXT, order_date TEXT)")
        purchase = [
                    ('Honda', 'Civic', '2017-07-12'),
                    ('Honda', 'Civic', '2017-08-13'),
                    ('Honda', 'Civic', '2017-08-25'),
                    ('Honda', 'Jazz', '2017-05-22'),
                    ('Honda', 'Jazz', '2017-07-25'),
                    ('Honda', 'Jazz', '2017-09-29'),
                    ('Ford', 'Fiesta', '2017-09-29'),
                    ('Ford', 'Fiesta', '2017-09-30'),
                    ('Ford', 'Fiesta', '2017-11-02'),
                    ('Ford', 'Focus', '2017-11-30'),
                    ('Ford', 'Focus', '2017-12-02'),
                    ('Ford', 'Focus', '2017-12-25'),
                    ('Ford', 'Fusion', '2017-12-31'),
                    ('Ford', 'Fusion', '2018-01-01'),
                    ('Ford', 'Fusion', '2018-01-20')
                    ]
        c.executemany("INSERT INTO orders VALUES (?, ?, ?)", purchase)


    except sqlite3.OperationalError:
        print("oops. something wrong. try again ...")

