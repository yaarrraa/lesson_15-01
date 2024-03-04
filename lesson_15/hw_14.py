class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return (f'First name: {self.first_name}\n'
                f'Last name: {self.last_name}\n'
                f'Gender: {self.gender}\n'
                f'Age: {self.age}')


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return (f'First name: {self.first_name}\n'
                f'Last name: {self.last_name}\n'
                f'Gender: {self.gender}\n'
                f'Age: {self.age}\n'
                f'Record book: {self.record_book}')


class GroupError(Exception):
    def __init__(self, message="Group is full! Unable to add new student"):
        self.message = message
        super().__init__(self.message)


class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        max_student = 10
        if len(self.group) >= max_student:
            raise GroupError
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


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод пошуку має повертати екземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!

try:
    for stud in range(10):
        gr.add_student(Student('Female', 25, 'Liza', 'Taylor', 'AN145'))
    gr.add_student(Student('Male', 30, 'Steve', 'Jobs', 'AN142'))
except GroupError as e:
    print(e)