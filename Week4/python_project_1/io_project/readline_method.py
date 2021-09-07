f = open("readme.txt", "r")
data = f.readline()
while data != '':   # Read the file 1 byte at a time
    data = data.strip("\n")  # Remove the newline characters from the end of each line
    print(data)
    data = f.readline()
f.close()
