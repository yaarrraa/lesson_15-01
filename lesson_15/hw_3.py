value_1=input("Please enter value_1 = ")
value_2=input("Please enter value_2 = ")
action=input ("Please select th action: '+', '-', '*', '/': ")

if action == "+":
    result_sum = int(value_1)+int(value_2)
    print(f"value_1 + value_2 = {result_sum}")
elif action == "-":
    result_minus = int(value_1)-int(value_2)
    print(f"value_1 - value_2 = {result_minus}")
elif action == "*":
    result_mult = int(value_1)*int(value_2)
    print(f"value_1 * value_2 = {result_mult}")
elif action == "/":
    if int(value_2)==0:
        print("Your value_2 cannot be 0")
    elif int(value_2)!=0:
        result_div = int(value_1)/int(value_2)
        print(f"value_1 / value_2 = {result_div}")



