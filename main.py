class Student:
    # метод для выставления оценок лекторам
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def srednee(self):
        sum_res = 0
        for grade in self.grades:
            sum_res += grade
        return sum_res / len(self.grades)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self):
        self.grades = {}


class Reviewer(Mentor):
    #метод выставления оценок студентам за ДЗ
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


student1 = Student('Сергей', 'Сперанский', 'муж')
student1.courses_in_progress = 'Python'
student1.finished_courses = 'GIT'
student1.grades = [9, 10, 8]
rate1 = Reviewer('Ivan', 'Ivanich')
rate1.rate_hw(student1, 'Python', 6)
print(student1.__dict__)
print(student1.srednee())
