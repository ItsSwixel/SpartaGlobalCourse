colours = ['black', 'red', 'green', 'blue']
print(colours)
print(colours[0])
colours[0] = "white"
colours.append("orange")
colours.remove("green")
print("Colours index orange before sort:", colours.index("orange"))
colours.sort()

print("Colours index orange after sort:", colours.index("orange"))

for colour in colours:
    print(colour)

print("red in colours?:", "red" in colours)
print("grey in colours?:", "grey" in colours)
print("Slice: ", colours[0:1])


print("---------------------------------------")
items = ['black', 1.5, True, 'red']

for item in items:
    print(item)

print(len(colours))
