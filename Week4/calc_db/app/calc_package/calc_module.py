def addition(val1: float = 0, val2: float = 0):
    return val1 + val2


def subtraction(val1, val2):
    return val1 - val2


# This is the subtraction function in lambda form
subtract = lambda val1, val2: val1 - val2


def multiplication(val1, val2):
    return val1 * val2


# This is a division function
def division(val1, val2):
    if val1 == 0 or val2 == 0:
        raise Exception("You cannot divide by 0")
    else:
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
        return result