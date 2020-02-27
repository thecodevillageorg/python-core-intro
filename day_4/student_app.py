
nameOfStudent= input('Enter name of student \n')
regNO=input('Enter the REG Number \n')

mathScore= int(input('Enter Math Score \n'))
engScore = int(input('Enter English Score \n'))
swaScore = int(input('Enter Swa Score \n'))

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
        'Unknown Grade'

def getMeanScore(score):
    return score/3

def getSum(a,b,c):
    return a+b+c

print('Exam Report for ',nameOfStudent,'\n')
print('MATH :',getGrade(mathScore),'\n')
print('ENG :',getGrade(engScore),'\n')
print('KISW :',getGrade(swaScore),'\n')
sum = getSum(mathScore,engScore,swaScore)
meanScore = getMeanScore(sum)
grade = getGrade(meanScore)

print('Mean Grade :',grade)
print('Mean Grade :',getGrade(getMeanScore(getSum(mathScore,engScore,swaScore))))



