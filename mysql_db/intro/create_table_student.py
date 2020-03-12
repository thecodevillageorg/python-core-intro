from db_functions import createDbConnection

dbConnection = createDbConnection()

mycursor = dbConnection.cursor()

mycursor.execute("CREATE TABLE student (id int(11) AUTO_INCREMENT primary key,reg_no VARCHAR(255), name VARCHAR(255), address VARCHAR(255), school_id int(11))")
