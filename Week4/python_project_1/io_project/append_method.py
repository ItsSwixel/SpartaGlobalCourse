f = open("readme.txt", "a+")
text = ["This is list line 1\n", "This is list line 2\n"]
f.write("This is the new line\n")
f.writelines(text)  # Will write each entry of a given list as a line
f.seek(0)
print(f.read())
f.close()
