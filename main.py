class Student:
    pass


class Mentor:
    def __init__(self, name, surname, courses):
        self.name = name
        self.surname = surname
        self.courses = courses

class Lecturer(Mentor):
    pass


class Reviewer(Mentor):
    pass