#Beep fine to count how many oodd and even numbers are
print("Please give me 3 whole numbers.")
print("first number:")
number1 = int(input())
print("your second number is:")
number2 = int(input())
print("and the last number, please:")
number3 = int(input())

even_numbers = 0
odd_numbers = 0

if number1 % 2 == 0:
    even_numbers = even_numbers + 1
else:
    odd_numbers = odd_numbers + 1
if number2 % 2 == 0:
    even = even_numbers + 1
else:
    odd_numbers = odd_numbers + 1
if number3 % 2 == 0:
    even = even_numbers + 1
else:
    odd_numbers = odd_numbers + 1
print()
print(f"There are {even_numbers} even numbers and {odd_numbers} odd numbers.")