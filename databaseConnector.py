import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="password",
  database="db471"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customer")
myresult = mycursor.fetchall()

for x in myresult: 
    print(x)