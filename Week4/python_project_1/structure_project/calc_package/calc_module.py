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
