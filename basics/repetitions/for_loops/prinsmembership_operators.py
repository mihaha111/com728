# Ask user for phrase
print("What phrase do you see?")
phrase = input()

# Identify markings
print("\nReversing...")
print("The phrase is ", end="")

reversed = ""

for letter in phrase:
    reversed = letter + reversed

print(reversed)

# To redo/think. didn't get it. simply copied from solution and even copied, still... didn't ring the bell
