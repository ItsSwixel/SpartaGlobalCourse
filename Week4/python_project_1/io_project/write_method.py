f = open("readme.txt", "w+")
f.write("This is the new line")

data = f.read()
print(data)
f.close()
