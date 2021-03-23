class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def srednee(self):
        sum1 = 0
        for student in Student:
            sum1 += student['grades']
            return sum1 / len(student)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def avg_geade(self, grades):
        sum_ex = 0
        for Student in grades:
            sum_ex += grades[grades]
            return sum_ex / len(grades)


class Reviewer(Mentor):
    pass


student1 = Student('One', 'DDD', 'man')
student1.courses_in_progress = 'Python'
student1.grades = 9, 10, 8
print(student1.__dict__)
print(student1.srednee)
