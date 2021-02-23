# Beeps is careful as some of the cables have live electricity
print("How many cables must I avoid?")
cables = int(input())
track_electric_cables = 0
while track_electric_cables <= cables:
    print(f"Avoiding...Done! {track_electric_cables} live cables avoided.")
    track_electric_cables = track_electric_cables + 1
print("\nAll live cables have been avoided")

#print("xxx", end="")