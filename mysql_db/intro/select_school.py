from db_functions import createDbConnection

dbConnection = createDbConnection()

mycursor = dbConnection.cursor()

mycursor.execute("SELECT * FROM school;")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)




