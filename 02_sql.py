# import the sqlite3 library
import sqlite3

# # create the connection object
# conn = sqlite3.connect("new.db")

# # get a cursor object used to execute sql command
# cursor = conn.cursor()

# # inser data
# cursor.execute("INSERT INTO population VALUES('New York City', 'NY', 8400000)")
# cursor.execute("INSERT INTO population VALUES('San Fransisco', 'CA', 800000)")

# # commit the change
# conn.commit()

# # close the database connection
# conn.close()

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    c.execute("INSERT INTO population VALUES('New York City', 'NY', 8400000)")
    c.execute("INSERT INTO population VALUES('San Fransisco', 'CA', 800000)")

