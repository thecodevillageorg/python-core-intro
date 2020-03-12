import mysql.connector

def getGrade(marks):
    if marks >= 80 and marks <= 100:
        return 'A'
    elif marks >= 60 and marks <80:
        return 'B'
    elif marks >= 40 and marks < 60:
        return 'C'
    elif marks >= 0 and marks < 40:
        return 'D'
    else:
        return 'Unknown Grade'


def getMeanScore(score):
    return score/3

def getSum(a,b,c):
    return a+b+c

# db connection
def createDbConnection():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="2423423423",
        database="codev_python"
    )
    return mydb



# create a school
def insertSchoolToDb(school):
    myDbConnection = createDbConnection()
    sql = "INSERT INTO school(code,name, address) VALUES (%s, %s,%s)"
    val = (school.code,school.name, school.address)
    mycursor=myDbConnection.cursor()
    mycursor.execute(sql, val)
    myDbConnection.commit()
    print(mycursor.rowcount, "record inserted.")

    ## fetch inserted shool to get id
    sqlSelect = "select * from school where code=%s"
    val=(school.code,)
    mycursor.execute(sqlSelect, val)
    insertedSchool = mycursor.fetchone()
    print(insertedSchool)
    for schl in insertedSchool:
        print(schl)

    return insertedSchool[0]




# find school by code


# create student
def insertStudentToDb(student):
    myDbConnection = createDbConnection()
    sql = "INSERT INTO student(reg_no,name,school_id) VALUES (%s,%s,%s)"
    val = (student.regNo,student.name,student.school.id)
    mycursor=myDbConnection.cursor()
    mycursor.execute(sql, val)
    myDbConnection.commit()
    print(mycursor.rowcount, "record inserted.")

    ## fetch inserted shool to get id
    sqlSelect = "select * from student where reg_no=%s"
    val=(student.regNo,)
    mycursor.execute(sqlSelect, val)
    insertedStudent = mycursor.fetchone()
    print(insertedStudent)
    for stdnt in insertedStudent:
        print(stdnt)

    # insert subjects
    print(student.subjects)
    insertSubjectToDb(student.subjects,insertedStudent[0])

    return insertedStudent[0]

# find student by reg no

# create a subject
def insertSubjectToDb(subjects,studentId):
    myDbConnection = createDbConnection()
    for subj in subjects:
        sql = "INSERT INTO subject(name,score,student_id) VALUES (%s,%s,%s)"
        val = (subj.name,subj.score,studentId)
        mycursor=myDbConnection.cursor()
        mycursor.execute(sql, val)
        myDbConnection.commit()
        print(mycursor.rowcount, "subject record inserted.")

# find by student id





