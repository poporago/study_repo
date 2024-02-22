import hellomodule
from hellomodule import Circle

print(hellomodule.a)
print(hellomodule.b)
print(hellomodule.C)

c = Circle(10)
print(c.넓이())
print(c.둘레())

from school.student import Student
from school.studentlist import StudentList

sl = StudentList()
sl. append(Student(100))
sl. append(Student(80))
sl. append(Student(85))


import school
from school import *

school.Student
school.StudentList