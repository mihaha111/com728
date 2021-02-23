#Bop is suming up numbers
print("How many numbers should I sum up?")
numbers = int(input())
crt = 1
sum = 0
while crt <= numbers:
    print(f"Please enter {crt}  of {numbers}:")
    x = int(input())
    crt = crt + 1
    sum = sum + x
print(f"The answer is {sum}")