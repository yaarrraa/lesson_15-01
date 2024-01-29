value_list = [0, 1, 0, 12, 3]

for value in value_list:
    if value == 0:
        value_list.remove(value)
        value_list.append(value)
print(value_list)




