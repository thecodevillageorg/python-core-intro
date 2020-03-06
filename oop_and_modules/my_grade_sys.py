
from my_functions import getGrade

import  my_functions


nameOfStudent= input('Enter name of student \n')
regNO=input('Enter the REG Number \n')

mathScore= int(input('Enter Math Score \n'))
engScore = int(input('Enter English Score \n'))
swaScore = int(input('Enter Swa Score \n'))

print('Exam Report for ',nameOfStudent,'\n')
print('MATH :',getGrade(mathScore),'\n')
print('ENG :',getGrade(engScore),'\n')
print('KISW :',getGrade(swaScore),'\n')
sum = my_functions.getSum(mathScore,engScore,swaScore)
meanScore = my_functions.getMeanScore(sum)
grade = getGrade(meanScore)

print('Mean Grade :',grade)
print('Mean Grade :',getGrade(my_functions.getMeanScore(my_functions.getSum(mathScore,engScore,swaScore))))



