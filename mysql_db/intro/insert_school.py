import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="23423432",
    database="codev_python"
)

mycursor = mydb.cursor()

sql = "INSERT INTO school (code,name, address) VALUES (%s, %s,%s)"
val = ("1001","Kiambu High School", "Kiambu")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

mycursor.execute("SELECT * FROM school;")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
