value_list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

for value in value_list:
    if value == 0:
        value_list.remove(value)
        value_list.append(value)
print(value_list)




