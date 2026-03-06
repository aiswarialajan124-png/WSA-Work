import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="wsaa"
)
print("Connection successful")

db.close()
