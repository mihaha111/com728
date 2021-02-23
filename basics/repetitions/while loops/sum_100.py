#Bop count all the numbers up to and included to 100
print("calculating the sum of the first 100 numbers...")
number = 0
sum = 0
while number <= 100:
    sum = sum + number
    number = number + 1

print(f"...Done! This answer: {sum}")