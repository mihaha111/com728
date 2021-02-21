#Counting (odds and even) without counting if only 3 numbers
print("Please give me 3 whole numbers - 2 digit.")
print("first number:")
number1 = int(input())
print("your second number is:")
number2 = int(input())
print("and the last number, please:")
number3 = int(input())

if (number1 + number2 + number3) % 2 == 0 and number1 % 2 == 0 and number2 % 2 == 0:
    print("There are 3 even numbers.")
elif (number1 + number2 + number3) % 2 != 0 and number1 % 2 == 0 and number2 % 2 == 0:
    print("We have 2 even number and 1 odd numbers.")
elif (number1 + number2 + number3) % 2 == 0 and number1 % 2 != 0 and number2 % 2 != 0:
    print("There are 2 odd numbers and 1 even number")
else:
    print("There are 3 odd numbers and 1 even number.")

print("done")

