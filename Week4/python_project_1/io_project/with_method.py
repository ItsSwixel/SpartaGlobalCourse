try:
    with open("readme.txt", "r") as f:
        print(f.read())  # Read entire file
        data2 = f.read(10)  # Read 10 bytes from where cursor is
        print(data2)
except PermissionError as err1:
    print(err1)
    print("You do not have access to this file")
except Exception as err:
    print(err)
