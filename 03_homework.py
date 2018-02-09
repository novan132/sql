# UPDATE and SELECT

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    try:
        c.execute("UPDATE inventory SET Quantity=10 WHERE Make='Honda' AND Model='Civic'")
        print("\nNEW DATA:\n")
        c.execute("SELECT * FROM inventory")
        
        rows = c.fetchall()

        for r in rows:
            print(r[0], r[1], r[2])
            
    except sqlite3.OperationalError:
        print("oops. something wrong, try again ...")

