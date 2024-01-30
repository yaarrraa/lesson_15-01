result = 0
value_1 = 0
value_2 = 0
action = 0

while True:
    value_1 = input("Please enter value_1 = ")
    value_2 = input("Please enter value_2 = ")
    action = input("Please select the action: '+', '-', '*', '/': ")
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
