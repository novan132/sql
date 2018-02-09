# JOINing multiple table

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    try:
        # retrieve data
        c.execute("""SELECT inventory.make, inventory.model,
            inventory.quantity, orders.order_date FROM inventory, orders
            WHERE inventory.model = orders.model""")

        rows = c.fetchall()

        for r in rows:
            print(r[0], r[1])
            print(r[2])
            print(r[3])
            print()
    except sqlite3.OperationalError:
        print("oops. something wrong. try again ...")

