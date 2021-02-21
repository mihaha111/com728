#Beep's breakfast
print("How would you like the eggs: omelette or egg yolks?")
eggs = input()
if eggs == 'omelette':
    print("What should I add: cheese, ham, mushrooms? Just 2 of them, please!")
    print("cheese: yes or no")
    val1 = 'cheese'
    answer1 = input()
    print("ham: yes or no")
    val2 = 'ham'
    answer2 = input()
    print("mushrooms: yes or no")
    val3 = 'mushrooms'
    answer3 = input()
    if answer1 == 'yes' and answer2 == 'yes' and answer3 == 'no':
        print(f"I love the omelette with {val1} and {val2} too!")
    elif answer1 == 'yes' and answer2 == 'no' and answer3 == 'yes':
        print("This is great! What would you like on top: ketchup or mayonnaise?")
        print("ketchup: yes or no")
        ans1 = input()
        print("mayonnaise: yes or no")
        ans2 = input()
        if ans1 == 'yes' and ans2 == 'no':
            print(f"Ok Beep, I will put ketchup on the top.")
        elif ans1 == 'no' and ans2 == 'yes':
            print(f"Ok Beep, I will put a little mayonnaise on it.")
        elif ans1 == 'no' and ans2 == 'no':
            print("I will put nothing on top of it.")
        else:
            print("Super. I will put both on top")
    elif answer1 == 'no' and answer2 == 'yes' and answer3 == 'yes':
        print("Beep this sounds interesting! How many mushrooms would you like?")
        mushrooms = int(input())
        if mushrooms < 10:
            print(f"Ok, I will add {mushrooms} mushrooms for you.")
        elif mushrooms >= 10:
            print(f"We don't have {mushrooms} mushrooms. Do you still want it with mushrooms?")
            a = input()
            if a == 'yes':
                print("Ok, so an omelette with ham and mushrooms.")
            else:
                print("An omelette without mushrooms")
    elif answer1 == 'yes' and answer2 == 'no' and answer3 == 'yes':
        print("Ok, will be an omelette with ham and mushrooms.")
    else:
        print("Error. Please choose 2 ingredients. If not...")
else:
    print("How many egg yolks would you like?")
    egg_yolks = int(input())
    print(f"Super, I will do {egg_yolks} yolks for you.")
print("\nEnjoy your breakfast, Beep!")

