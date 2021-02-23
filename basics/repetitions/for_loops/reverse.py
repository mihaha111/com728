#Beep and Bop reading a book in which everithing is written backwords
print("What phrase do you see?")
phrase = input()
print("Reversing...")
print("\nThe phrase is:")
for position in range(len(phrase) - 1, -1, -1):
    print(phrase[position], end="")
print()
print("\nDone!")


#!!!! For POSITION PRINT NO f and NO "  !!!!!!