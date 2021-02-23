#Beep needs to know how many bars should be charged
print("How many bars should be charged?")
bars = int(input())
number_of_bars_charged = 0
while number_of_bars_charged <= bars:
    print(f"Charging: {number_of_bars_charged * ' █ '}")
    number_of_bars_charged = number_of_bars_charged +1
print("\nThe battery is fully charged!")