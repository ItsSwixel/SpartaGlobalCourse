f = None
try:
    f = open("readme.txt", "x")  # x mode only creates a new file and if it exists it errors
except FileExistsError as err:
    print(err)
    print("This file already exists and therefore cannot be created")
except Exception as exception_msg:
    print(exception_msg)
finally:
    try:
        f.close()
    except AttributeError as err1:
        exit()
"""f.write("This is the new line\n")
f.seek(0)
print(f.read())
f.close()
"""