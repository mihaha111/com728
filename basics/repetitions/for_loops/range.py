#The light level of Beep and Bop's night vision
print("What level of brightness is required for Beep?")
level_Beep = int(input())
print("What level of brightness is required for Bop?")
level_Bop = int(input())
if level_Beep % 2 == 0 and level_Bop % 2 == 0:
    for count in range(0, level_Beep, 2):
        print(f"Beep's brightness level: {level_Beep * '*'}")
        level_Beep = level_Beep + 2
    for count in range(0, level_Bop, 2):
        print(f"Bop's brightness level: {level_Bop * '*'}")
        level_Bop = level_Bop + 2
    print("\nAdjustments complete!")
else:
    print("\nPlease, enter even numbers.")
