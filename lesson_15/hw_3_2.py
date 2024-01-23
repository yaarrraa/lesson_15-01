value_list = [1,2,3]
lenth = len(value_list)
print(f"Lenth of the list is {lenth}")
print(f"value_list = {value_list}")

if lenth == 0:
    print(f"Lenth of the list is 0 {value_list}")
elif lenth == 1:
    print(f"value_list = {value_list}")
elif lenth > 1:
    value_list.insert(0, value_list[-1])
    value_list.pop()
    print(value_list)
