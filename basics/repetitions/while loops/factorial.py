#Bop wants to calculate a factorial number
print("Please enter a number:")
number = int(input())
crt = 0
prod = 1
while crt < number:
    crt = crt + 1
    prod = prod * crt
print(f"The factorial is {prod}")


#one tab for inside loop
#if <= will factorial * following number (ie 5! = 720 - (1*2*3*4*5)*6
