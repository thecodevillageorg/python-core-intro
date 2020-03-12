'''
python3 -m pip install mysql-connector

'''
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="5464646",
  port="3306"
)

# print(mydb)

'''
Connect to the database
'''
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE codev_python")

