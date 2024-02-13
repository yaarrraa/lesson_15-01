def add_one(some_list):
    digits = 0
    for digit in some_list:
        digits = digits * 10 + digit
    new_digit_str = str(digits + 1)
    new_list = []
    for dig in new_digit_str:
        new_list.append(int(dig))
    return new_list


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")


def add_one_2(some_list):
    digits = 0
    for digit in some_list:
        digits = digits * 10 + digit
    new_list = list(map(int, str(digits + 1)))
    return new_list


assert add_one_2([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one_2([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one_2([0]) == [1], 'Test3'
assert add_one_2([9]) == [1, 0], 'Test4'
print("ОК")
