#How many steps are left to be done to the cave?
print("How far are we from the cave?")
steps = int(input())
for count in range(steps, 0, -1):
    print(f"{steps} steps remaining")
    steps = steps - 1
print("\nWe have reached the cave!")
