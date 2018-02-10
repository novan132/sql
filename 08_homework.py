import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()
    try:
        sql = {
            'Civic': "SELECT DISTINCT inventory.make, inventory.model, inventory.quantity, count(orders.order_date) \
            FROM inventory, orders WHERE inventory.Model = 'Civic' AND orders.model = 'Civic'",
            'Jazz': "SELECT DISTINCT inventory.make, inventory.model, inventory.quantity, count(orders.order_date) \
            FROM inventory, orders WHERE inventory.Model = 'Jazz' AND orders.model = 'Jazz'",
            'Fiesta': "SELECT DISTINCT inventory.make, inventory.model, inventory.quantity, count(orders.order_date) \
            FROM inventory, orders WHERE inventory.Model = 'Fiesta' AND orders.model = 'Fiesta'",
            'Focus': "SELECT DISTINCT inventory.make, inventory.model, inventory.quantity, count(orders.order_date) \
            FROM inventory, orders WHERE inventory.Model = 'Focus' AND orders.model = 'Focus'",
            'Fusion': "SELECT DISTINCT inventory.make, inventory.model, inventory.quantity, count(orders.order_date) \
            FROM inventory, orders WHERE inventory.Model = 'Fusion' AND orders.model = 'Fusion'"
        }
        
        for key, value in sql.items():
            c.execute(value)
            result = c.fetchone()
            print(result[0], result[1], result[2])
            print("order count: ", result[3])
            print()

    except sqlite3.OperationalError:
        print("oops. something wrong. try again ...")