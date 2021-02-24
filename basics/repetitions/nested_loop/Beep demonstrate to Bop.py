#Beep demonstrates to Bop that for any long number you can check if the numer divides by 3
# if the sum of the all digits of the number divides by 3
print("Bop,I can show you how to  check if a 5 digit long number divides by 3")
print("We will add the digits of the number and if there sum divides by 3, the number will do")
print("Bop give me a 5 digits long number, each digit at a time:")
digit1 = int(input())
digit2 = int(input())
digit3 = int(input())
digit4 = int(input())
digit5 = int(input())
print(f"\nYour number is: {digit1}{digit2}{digit3}{digit4}{digit5}")
print("To confirm this is your number please type it in:")
long_number = int(input())
print(f"Ok, the sum of {digit1} + {digit2} + {digit3} + {digit4} + {digit5} = {digit1 + digit2 + digit3 + digit4 + digit5}")
print(f"Let us check if this sum {digit1 + digit2 + digit3 + digit4 + digit5} divides by 3")
print("\n\tBonus: I will also tell you how many numbers up to this number will divide by 3")
count = 0
number = 0
if long_number % 3 == 0:
    print("\nYes, this number divides by 3!")
    for number in range(0, long_number, 1):
        if number % 3 == 0:
            count = count + 1
            number = number + 1
        else:
            number = number + 1
            count = count
    print(f"There are {count} numbers that divide by 3 up to {long_number}")
else:
    print("\nOps, This number doesn't divide by 3.")
print("\nDid you like it?")


#error works but not properly how to incorporate



