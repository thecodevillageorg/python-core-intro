from db_functions import createDbConnection

dbConnection = createDbConnection()

mycursor = dbConnection.cursor()

mycursor.execute("CREATE TABLE subject (id int(11) AUTO_INCREMENT primary key, name VARCHAR(255),  score int(11),student_id int(11))")
