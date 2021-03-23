class Student:
    name = ''
    age = 0
    course = ''


sergey = Student()
sergey.name = 'Сергей Сперанский'
sergey.age = 36
sergey.course = 'Python'
sergey.grade = 2
print(sergey.__dict__)
