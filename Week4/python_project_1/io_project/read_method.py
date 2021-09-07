f = open("readme.txt", "r")
print(f.read())  # Read entire file
data2 = f.read(10)  # Read 10 bytes from where cursor is
print(data2)
f.close()
