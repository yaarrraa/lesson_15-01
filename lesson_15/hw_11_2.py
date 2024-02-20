def is_even(number):
    str_num = str(number)
    last_digit = str_num[-1]
    return last_digit in ["0", "2", "4", "6", "8"]


assert is_even(2494563894038 ** 2) == True, 'Test1'
assert is_even(1056897 ** 2) == False, 'Test2'
assert is_even(24945638940387 ** 3) == False, 'Test3'
print('Ok')
