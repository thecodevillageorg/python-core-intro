'''
python -m pip install mysql-connector

'''
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="2342342",
  database="codev_python"
)


mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE school (id int(11) AUTO_INCREMENT primary key,code VARCHAR(255), name VARCHAR(255), address VARCHAR(255))")