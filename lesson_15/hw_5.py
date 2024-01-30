my_string = input("Please enter your variable: ")
condition_1 = my_string.isidentifier()

if condition_1:
    if my_string == "_":
        print("True")
    else:
        condition_2 = my_string.islower()
        print(condition_2)
else:
    print(condition_1)


