print("How many columns would you like?")
rows = int(input())
print("\nHow many rows would you like?")
columns = int(input())
print("\nPlease enter at your choice 3 consecutive symbols")
symbols = input()
for column in range(0, columns, 1):
    for row in range(0, rows, 1):
        print(f"{symbols} ", end="")
    print()
print("\nDone!")