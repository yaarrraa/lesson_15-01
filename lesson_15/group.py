from human import Human
from student import Student

class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        self.group.add(student)

    def delete_student(self, last_name):
        student_to_remove = self.find_student(last_name)
        if student_to_remove is not None:
            self.group.remove(student_to_remove)

    def find_student(self, last_name):
        for student in self.group:
            if last_name == student.last_name:
                return student

    def __str__(self):
        all_students = ''
        for student in self.group:
            all_students += str(student.first_name) + " " + str(student.last_name) + ", "
        return f'Number:{self.number}\n{all_students} '