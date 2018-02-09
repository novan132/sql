# create sqlite3 database and table

# import sqlite3 library
import sqlite3

# create new database if the database doesn't already exist
conn = sqlite3.connect("new.db")

# get cursor object used to execute sql command
cursor = conn.cursor()

# create a table
cursor.execute("CREATE TABLE population (city TEXT, state TEXT, population INT)")

# close the database connection
conn.close()