from db_functions import createDbConnection

dbConnection = createDbConnection()

mycursor = dbConnection.cursor()

sql = "SELECT * FROM school WHERE code ='1001'"

sql = "SELECT * FROM school WHERE id ='5'"
mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)