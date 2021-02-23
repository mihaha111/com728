#Beep and Bop in cave and Beep sees some strange symbols on the wall
print("What strange markings do you see?")
characters = input()
chr = 0
print("Identifying...")
print()
for position in range(0, len(characters), 1):
    print(f"index {chr}: {characters[position]}")
    chr = chr + 1
print("\nDone!")



