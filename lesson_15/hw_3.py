value_1=input("Please enter value_1 = ")
value_2=input("Please enter value_2 = ")
action=input ("Please select the action: '+', '-', '*', '/': ")

if action == "+":
    result_sum = float(value_1)+float(value_2)
    print(f"value_1 + value_2 = {result_sum}")
elif action == "-":
    result_minus = float(value_1)-float(value_2)
    print(f"value_1 - value_2 = {result_minus}")
elif action == "*":
    result_mult = float(value_1)*float(value_2)
    print(f"value_1 * value_2 = {result_mult}")
elif action == "/":
    if float(value_2) == 0.0:
        print("Your value_2 cannot be 0")
    elif float(value_2) != 0.0:
        result_div = float(value_1)/float(value_2)
        print(f"value_1 / value_2 = {result_div}")



