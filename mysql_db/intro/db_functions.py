
import mysql.connector

def createDbConnection():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="5345345",
        database="codev_python"
    )
    return mydb