'''
Nested Dictionaries
'''

students = dict()

student1 = dict()
student1['name'] = "Toma"
student1['class'] = 'Form 1'
student1['regNo'] = '7878787'

student2 = dict()
student2['name'] = "Jane"
student2['class'] = 'Form 2'
student2['regNo'] = '242342'

students['1'] = student1
students['2'] = student2

print(students)
print(len(students))
print(students.get('1'))