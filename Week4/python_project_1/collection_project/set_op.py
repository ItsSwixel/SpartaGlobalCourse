colours = {'black', 'grey', 'red', 'blue', 'green'}

print(colours)

for i in colours:   # Won't always print in the same order so only useful if order doesn't matter
    print(i)

colours.add("white")
print(colours)

colours.discard("grey")
print(colours)

print("============ Math & Sets ============")
colours1 = {'black', 'grey', 'red'}
colours2 = {'black', 'blue'}

print(colours1)
print(colours2)

print("Intersect:", colours1 & colours2)
print("Union:", colours1 | colours2)
print("Difference:", colours1 - colours2)
print("Superset:", colours1 > colours2)

items = set(("coffee", "tea", "black", "white"))
