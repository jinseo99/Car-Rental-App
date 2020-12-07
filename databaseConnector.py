import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="password",
  database="db471"
)
mycursor = mydb.cursor()
# mycursor.execute("INSERT INTO `customer` (`Customer_ID`, `Customer_Name`, `Phone_Number`, `Address`) VALUES ('2', 'name2', 'phone2', 'add2');")
mycursor.execute("SELECT * FROM customer")
myresult = mycursor.fetchall()

for x in myresult: 
    print(x)