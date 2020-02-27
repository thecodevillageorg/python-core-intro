
nofsubjects= int(input('Enter no. of subjects \n'))
subjectScores = dict()
n=1

def getGrade(marks):
    if marks > 80:
        return 'A'
    elif marks > 60 and marks <80:
        return 'B'
    elif marks > 40 and marks < 60:
        return 'C'
    else:
        return 'D'

def getMeanScore(marks,noOfSubjects):
    return marks/noOfSubjects

def getSubjectInput():
    subjectName = input('Enter name of Subject \n'.strip())
    subjectSCore = int(input('Enter the score for {} \n'.format(subjectName)))
    subjectScores[subjectName] = subjectSCore
    
print(n)
while n <= nofsubjects:
    getSubjectInput()
    n += 1

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



    

getReportBook(subjectScores)



# print('Exam Report for ',nameOfStudent,'\n')
# print('MATH :',getGrade(mathScore),'\n')
# print('ENG :',getGrade(engScore),'\n')
# print('KISW :',getGrade(swaScore),'\n')
# print('Mean Grade :',getGrade(getMeanScore(mathScore+engScore+swaScore)))



