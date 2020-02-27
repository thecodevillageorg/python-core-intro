
nameOfStudent= input('Enter name of student \n')
regNO=input('Enter the REG Number \n')

mathScore= int(input('Enter Math Score \n'))
engScore = int(input('Enter English Score \n'))
swaScore = int(input('Enter Swa Score \n'))

subjectScores = dict()


def getSubjectInput():
    subjectName = input('Enter name of Subject \n'.strip())
    subjectSCore = int(input('Enter the score for ',subjectName))
    subjectScores[subjectName] = subjectSCore
    


def getGrade(marks):
    if marks > 80:
        return 'A'
    elif marks > 60 and marks <80:
        return 'B'
    elif marks > 40 and marks < 60:
        return 'C'
    else:
        return 'D'

def getMeanScore(marks):
    return marks/3

print('Exam Report for ',nameOfStudent,'\n')
print('MATH :',getGrade(mathScore),'\n')
print('ENG :',getGrade(engScore),'\n')
print('KISW :',getGrade(swaScore),'\n')
print('Mean Grade :',getGrade(getMeanScore(mathScore+engScore+swaScore)))



