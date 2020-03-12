from school import School
from student import Student
from subject import Subject
from my_functions import getGrade
from my_functions import insertSchoolToDb
from my_functions import insertStudentToDb

noOfStudents = int(input('Enter the no of students'))

students = []
# input details for many students
for n in range(1,noOfStudents+1):
    studentName = input('Enter Name of Student \n')
    regNo = input('Enter Reg Number \n')

    schoolCode= input('Enter School Code \n')
    schoolName = input('Enter Name of School \n')
    schoolAddress = input('Enter School Address \n')
 

    school = School(0,schoolCode,schoolName,schoolAddress)
    # insert school to a database
    schoolid = insertSchoolToDb(school)
    school.id = schoolid


    nofsubjects= int(input('Enter no. of subjects \n'))
    subjects = []
    for s in range(1,nofsubjects+1):
        subjectName = input('Enter name of Subject \n'.strip())
        subjectSCore = int(input('Enter the score for {} \n'.format(subjectName)))
        subject = Subject(subjectName,subjectSCore)
        subjects.append(subject)
        # insert subject to database


    student = Student(studentName,regNo,school,subjects)
    # print(student.name)
    # print(student.school.name)
    students.append(student)
    # insert student to database
    studentid = insertStudentToDb(student)
    



for stdnt in students:
    print(stdnt.name,stdnt.school.name,len(stdnt.subjects))
    for subject in subjects:
        print(subject.name,':',subject.score,'Grade : ',getGrade(subject.score))