import sqlite3

with sqlite3.connect("newnum.db") as connection:
    c = connection.cursor()

    prompt = """
            Select the operation you want to perform [1-5]
            1. Average
            2. Max
            3. Min
            4. Sum
            5. Exit
            """

    while True:
        x = input(prompt)

        if x in set(["1", "2", "3", "4"]):
            try:
                operation = {1: 'avg', 2: 'max', 3: 'min', 4: 'sum'}[int(x)]
                c.execute("SELECT {}(num) FROM numbers".format(operation))
                result = c.fetchone()
                print(operation, ": %f" % result[0])
                print()

            except sqlite3.OperationalError:
                print("oops. something wrong. try again ...")
        elif x == "5":
            print("exit")
            break

    
