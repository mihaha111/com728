#Beep finds an other robot in the dark forest, stucked in cables, so he try to save him.
print("How many cables should I remove?")
cables = int(input())
removed_cables = 1
while removed_cables < cables:
      removed_cables = removed_cables + 1
print(f"removed {removed_cables} cables")

# my error!!! in while i put invers count and print with f ...it will print f-str for a lot lot many times