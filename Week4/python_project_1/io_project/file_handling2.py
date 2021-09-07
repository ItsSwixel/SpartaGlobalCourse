f = open("readme.txt", "r")
data = f.read(1)
while data != '':   # Read the file 1 byte at a time
    print(data)
    data = f.read(1)
f.close()
