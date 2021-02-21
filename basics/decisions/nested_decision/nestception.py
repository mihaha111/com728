#Looking for batteries
print("Where should I look for batteries: bedroom, bathroom or lab?")
place = input()
if place == 'bedroom':
    print("Where in the bedroom should I look: under the bed?")
    under_the_bed = input()
    if under_the_bed == 'yes':
        print("Found some shoes, but no batteries.")
    else:
        print("In this bedroom found only mess, no batteries!")
elif place == 'bathroom':
    print("Where in the bathroom should I look: in the bathtub?")
    bathtube = input()
    if bathtube == 'yes':
        print("Found a rubber duck, but no batteries!")
    else:
        print("Is the door locked?")
elif place == 'lab':
    print("Where should I look: under the table?")
    table = input()
    if table == 'yes':
        print("Yes! I found my battery!")
    else:
        print("Found some tools, but no batteries.")
else:
    print(f"\n\tI don't think the batteries could be in the {place}, but I can try.")



