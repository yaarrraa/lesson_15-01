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