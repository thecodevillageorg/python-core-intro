

def getGrade(marks):
    if marks >= 80:
        return 'A'
    elif marks >= 60 and marks <80:
        return 'B'
    elif marks >= 40 and marks < 60:
        return 'C'
    else:
        return 'D'

def getMeanScore(marks,noOfSubjects):
    return marks/noOfSubjects



# def getSubjectInput():
#     subjectName = input('Enter name of Subject \n'.strip())
#     subjectSCore = int(input('Enter the score for {} \n'.format(subjectName)))
#     subjectScores[subjectName] = subjectSCore

def getReportBook(dictionary):
    totalMarks = 0
    output = ''
    for subject, score in dictionary.items():
        print(subject,score)
        totalMarks += score
        output += subject +': ' + getGrade(score) +' \n'.format(dictionary[subject])
    print(output)
    print('TOTAL Marks:',totalMarks)
    meanscore=getMeanScore(totalMarks,len(dictionary))
    print('MEAN SCORE:',meanscore)
    print('MEAN GRADE:',getGrade(meanscore))

    print('MEAN GRADE WITH FUNCTION CHAINING:',getGrade(getMeanScore(totalMarks,len(dictionary))))





# multiple students
students = dict()

# no of students
noOfStudents = int(input('Enter the no of students'))

# input details for many students
for n in range(1,noOfStudents+1):
    student = dict()
    studentName = input('Enter Name of Student \n')
    regNo = input('Enter Reg Number \n')
    studentClass = input('Enter Class \n')
    student['name'] = studentName
    student['RegNo'] = regNo
    student['class'] = studentClass
    nofsubjects= int(input('Enter no. of subjects \n'))
    subjects = dict()

    for s in range(1,nofsubjects+1):
        subjectName = input('Enter name of Subject \n'.strip())
        subjectSCore = int(input('Enter the score for {} \n'.format(subjectName)))
        subjects[subjectName] = subjectSCore

    student['scores'] = subjects
    students[regNo] = student

# print(students)

# {'name': 'Dan', 'RegNo': '23342', 'class': '3', 'scores': {'Chem': 80, 'PHY': 30, 'BIO': 67}}

print('************* REPORT CARD ******')
for k,v in students.items():
    print('Name:',v['name'])
    print('Reg No:',v['RegNo'])
    print('Class:',v['class'])
    totalMarks = 0
    for subject,score in v['scores'].items():
        totalMarks += score
        print(subject,score,"GRADE :",getGrade(score))
    print('MEAN SCORE :',getMeanScore(totalMarks,len(v['scores'])))

    print('MEAN GRADE :',getGrade(getMeanScore(totalMarks,len(v['scores']))))


print('*************END REPORT CARD ******')







# print('Exam Report for ',nameOfStudent,'\n')
# print('MATH :',getGrade(mathScore),'\n')
# print('ENG :',getGrade(engScore),'\n')
# print('KISW :',getGrade(swaScore),'\n')
# print('Mean Grade :',getGrade(getMeanScore(mathScore+engScore+swaScore)))



