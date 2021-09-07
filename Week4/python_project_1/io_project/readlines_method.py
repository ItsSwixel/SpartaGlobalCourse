f = open("readme.txt", "r")
data = f.readlines()    # Reads the lines and puts each line as an entry in a list
print(data[0].strip("\n"))
print(data[1])
f.close()
