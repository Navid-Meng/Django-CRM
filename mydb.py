import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user = 'root',
    passwd = '',
)

cursor_object = database.cursor()

cursor_object.execute("CREATE DATABASE elderco")

print("All done!")