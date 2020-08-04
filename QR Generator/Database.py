import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Tallarico1973!"
)

print(mydb)