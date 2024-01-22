number = input("Please enter your number: ")
print("Your number is " + number)
numeral_1 = int(number)//1000
print(numeral_1)
numeral_2 = (int(number)%1000)//100
print(numeral_2)
numeral_3 = (int(number)%100)//10
print(numeral_3)
numeral_4 = int(number)%10
print(numeral_4)