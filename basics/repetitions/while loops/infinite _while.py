print("Would you like to know how many numbers divide by 3 up to a number? Please enter a number:")
number = int(input())
print(f"Ok, so this is your number is {number}")
previous = 1
count = 0

while number % 3 == 0:
    print(f"\n Yuppy! Your number {number} divides by 3")
    print(f"there are {count} numbers that divide by 3 up to your number {number}")
    count = count + 1
    previous = previous +1

print(f"\n Yuppy! Your number {number} divides by 3")
print(f"there are {count} numbers that divide by 3 up to your number {number}")

print(f"\nYour number {number} doesn't divide by 3")

# how to take out the float numbers from counting?
