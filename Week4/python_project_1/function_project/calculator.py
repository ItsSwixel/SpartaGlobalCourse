import os


def addition(val1: float = 0, val2: float = 0):
    file_write(val1 + val2)
    return val1 + val2


def subtraction(val1, val2):
    file_write(val1 - val2)
    return val1 - val2


# This is the subtraction function in lambda form
subtract = lambda val1, val2: val1 - val2


def multiplication(val1, val2):
    file_write(val1 * val2)
    return val1 * val2


# This is a division function
def division(val1, val2):
    if val1 == 0 or val2 == 0:
        raise Exception("You cannot divide by 0")
    else:
        file_write(val1 / val2)
        return val1 / val2


def division_with_exception(val1, val2):
    try:
        result = val1 / val2
    except ZeroDivisionError as err:
        print(err)
        return "Division by zero exception"
    except Exception as general_err:
        print(general_err)
        return "Unknown division error"
    else:
        file_write(result)
        return result
    finally:
        # This will run whether an exception happens or not
        print("This is the finally block of code")


def file_write(value):
    f = open("func_results.txt", "a+")
    f.write(str(value) + "\n")
    f.close()


def print_result(val1, val2, operation, result, description="No description"):
    # print("{} {} {} = {}".format(val1, operation, val2, result))
    print(f"{val1} {operation} {val2} = {result} | {description}")  # New and better way
    return


def main():
    num1 = float(input("Please enter your first number: "))
    num2 = float(input("Please enter your second number: "))
    print_result(num1, num2, "+", addition(val1=num1, val2=num2), "This is a sum operation")
    print_result(num1, num2, "-", subtraction(num1, num2))
    # print_result(num1, num2, "-", subtract(num1, num2), "Subtraction using lambda")
    print_result(num1, num2, "*", multiplication(num1, num2))
    # print_result(num1, num2, "/", division(num1, num2))
    # assert num1 != 0, "Sorry, number 1 should not be zero. (Using assert method)"
    print_result(num1, num2, "/", division_with_exception(num1, num2))
    return


if os.path.isfile("func_results.txt"):
    option = input("Would you like to remove the current results file? Yes or No ").upper()
    if option == "YES":
        os.remove("func_results.txt")

for i in range(0, 5):
    main()
