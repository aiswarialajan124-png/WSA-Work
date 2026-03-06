import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="wsaa"
)

cursor = db.cursor()

cursor.execute("SELECT * FROM student")

for row in cursor.fetchall():
    print(row)

cursor.close()
db.close()