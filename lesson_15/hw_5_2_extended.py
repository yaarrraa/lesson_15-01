result = 0
value_1 = 0
value_2 = 0
action = 0
while True:
    is_true = True
    while is_true:
        value_1 = input("Please enter value_1 = ")
        if value_1.isdigit():
            is_true = False
            break
        else:
            print("Please enter only digits")
    is_true = True
    while is_true:
        value_2 = input("Please enter value_2 = ")
        if value_2.isdigit():
            is_true = False
            break
        else:
            print("Please enter only digits")
    is_true = True
    while is_true:
        action = input("Please select the action: '+', '-', '*', '/': ")
        if action not in ("+", "-", "*", "/"):
            print("invalid method")
        else:
            is_true = False
            break
    if action == "+":
        result = float(value_1) + float(value_2)
    elif action == "-":
        result = float(value_1) - float(value_2)
    elif action == "*":
        result = float(value_1) * float(value_2)
    elif action == "/":
        if float(value_2) == 0.0:
            result = "ERROR - can't divide by zero"
        elif float(value_2) != 0.0:
            result = float(value_1) / float(value_2)
    print(result)
    c = input("Do you want to continue? Enter yes/no: ")
    if c != "yes":
        break
