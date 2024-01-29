value_list = [1, 0, 3]
lenth = len(value_list)

sum_of_numbers = 0
result = 0

if lenth == 0:
    print(f"Result = {result}")
else:
    for number in range(0, lenth, 2):
        sum_of_numbers += value_list[number]
        result = sum_of_numbers * value_list[-1]
    print(f"Result = {result}")
