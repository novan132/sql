# INSERT command with error handler

# import sqlite3 library
import sqlite3

# create connection object
conn = sqlite3.connect("new.db")

# get cursor object to execute SQL command
cursor = conn.cursor()

try:
    # insert data
    cursor.execute("INSERT INTO populations VALUES('New York City', 'NY', 8400000)")
    cursor.execute("INSERT INTO populations VALUES('San Fransisco', 'CA', 800000)")

    # commit the change
    conn.commit()
except sqlite3.OperationalError:
    print("Ooops! something went wrong. Try again ...")

# close the database connection
conn.close()

