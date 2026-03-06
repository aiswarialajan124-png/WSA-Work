import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="wsaa"
)

cursor = db.cursor()

sql = "INSERT INTO student (firstname, age) VALUES (%s,%s)"
values = ("Mary", 21)

cursor.execute(sql, values)

db.commit()

print("Inserted ID:", cursor.lastrowid)

cursor.close()
db.close()