# How to determinate the ASCII code for a character
print("Program Started!")
print("Please enter a standard character:")
character = input()
if len(character) == 1:
    print(f"The MORSE code for {character} is {ord(character)}")
else:
    print("A single character was expected.")
print("\nProgram Ended!")

# how it knows it is ASCII if I have not import or any define function for ASCII
# it change with MORSE it will give me for o = 111 O = 79 and for s = 115 S = 83
# MORSE HAS BEEN CONVERTED TO ASCII! NICE ONE!!! THIS IS WHY ASCII IS IMPORANT???
# SOS in MORSE is ...___... (3 short; 3 long; 3 3 short) = ASCII 837983,
#!!!!as else will be  464646959595464646 - or something alike
# how would I know which the program already now vs to import or call vs to define????