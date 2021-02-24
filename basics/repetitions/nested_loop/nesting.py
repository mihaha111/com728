#Distance between 2 markers
print("Please enter a long sequence made of 2 symbols and use one of them for 2 times only ")
sequence = input()
print("Which symbol did you used twice? This will be our marker.")
marker = input()
is_counting = False
count = 0
for character in sequence:
    if (is_counting == False) and  character == marker:
        print("Found first marker.")
        is_counting = True
    elif (is_counting == True) and character == marker:
        print("Found the second marker.")
    elif is_counting:
        count += 1
print(f"\nThe distance between the markers is {count}")

# how to define marker = x




