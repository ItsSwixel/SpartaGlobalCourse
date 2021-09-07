import os
from calc_package import calc_module


def print_result(val1, val2, operation, result, description="No description"):
    # print("{} {} {} = {}".format(val1, operation, val2, result))
    print(f"{val1} {operation} {val2} = {result} | {description}")  # New and better way
    return


def main():
    num1 = float(input("Please enter your first number: "))
    num2 = float(input("Please enter your second number: "))
    print_result(num1, num2, "+", calc_module.addition(val1=num1, val2=num2), "This is a sum operation")
    print_result(num1, num2, "-", calc_module.subtraction(num1, num2))
    # print_result(num1, num2, "-", subtract(num1, num2), "Subtraction using lambda")
    print_result(num1, num2, "*", calc_module.multiplication(num1, num2))
    # print_result(num1, num2, "/", division(num1, num2))
    # assert num1 != 0, "Sorry, number 1 should not be zero. (Using assert method)"
    print_result(num1, num2, "/", calc_module.division_with_exception(num1, num2))
    return


if os.path.isfile("func_results.txt"):
    option = input("Would you like to remove the current results file? Yes or No ").upper()
    if option == "YES":
        os.remove("func_results.txt")

for i in range(0, 1):
    main()
