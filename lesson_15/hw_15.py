import numbers


class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return round(self.width * self.height)

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.get_square() == other.get_square()

    def __add__(self, other):
        total_area = self.get_square() + other.get_square()
        total_width = total_area ** 0.5
        total_height = total_area ** 0.5
        return Rectangle(total_width, total_height)

    def __mul__(self, n):
        if isinstance(n, numbers.Real):
            total_area_number = self.get_square() * n
            total_width_number = total_area_number ** 0.5
            total_height_number = total_area_number ** 0.5
        return Rectangle(total_width_number, total_height_number)

    def __str__(self):
        return f"Rectangle [width = {self.width}, height = {self.height}]"


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2
assert r3.get_square() == 26, 'Test3'

r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'
