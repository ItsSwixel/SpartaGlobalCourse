def addition(val1, val2):
    return val1 + val2


def subtraction(val1, val2):
    return val1 - val2


def multiplication(val1, val2):
    return val1 * val2


def division(val1, val2):
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
