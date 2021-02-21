#Classifing Beep's books
print("What type of cover does the book have: hard or soft?")
cover = input()
if cover == 'soft':
    print("Is the book perfect bound: yes or no?")
    perfect_bound = input()
    if perfect_bound == 'yes':
        print("Soft cover, perfect bound books are very popular!")
    elif perfect_bound == 'no':
        print("Soft covers with coils or stitches are great for short books.")
else:
    print("Books with hard covers can be more expansive!")
print("\nHowever, it is so nice to feel any type of book in your hands!")
