import module2


def welcome_module1():
    print("Welcome from module1 - welcome_module1 function")


def main():
    print("This is module 1")
    welcome_module1()
    module2.welcome_module2()


if __name__ == "__main__":
    main()
