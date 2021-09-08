import os
from calc_package import calc_module
import json

JSON_objects = {}
results = {}
counter = 1


def dict_storage(data):
    results[data[1]]=(str(data[0]) + data[1] + str(data[2]) + "=" + str(data[3]))
    return


def print_result(data):
    # print("{} {} {} = {}".format(val1, operation, val2, result))
    print(f"{data[0]} {data[1]} {data[2]} = {data[3]} | {data[4]}")  # New and better way
    return


def main():
    num1 = int(input("Please enter your first number: "))
    num2 = int(input("Please enter your second number: "))
    addition = (num1, "+", num2, calc_module.addition(val1=num1, val2=num2), "")
    print_result(addition)
    dict_storage(addition)
    JSON_objects[counter] = results
    subtraction = (num1, "-", num2, calc_module.subtraction(num1, num2), "")
    print_result(subtraction)
    dict_storage(subtraction)
    multiplication = (num1, "*", num2, calc_module.multiplication(num1, num2), "")
    print_result(multiplication)
    dict_storage(multiplication)
    # assert num1 != 0, "Sorry, number 1 should not be zero. (Using assert method)"
    division = (num1, "/", num2, calc_module.division_with_exception(num1, num2), "")
    print_result(division)
    dict_storage(division)
    return


if __name__ == "__main__":
    if os.path.isfile('results.json'):
        with open('results.json', 'r') as f:
            JSON_objects = json.load(f)
        counter = len(JSON_objects)+1

    for i in range(0, 3):
        main()
        JSON_objects[counter] = results
        counter += 1
        results = {}

    with open('results.json', 'w') as f:
        json.dump(JSON_objects, f, indent=4)
