from calc_package import calc_module
import sqlite3
from contextlib import closing


def add_database(data):
    with closing(sqlite3.connect("data.db")) as connection:
        with closing(connection.cursor()) as cursor:
            equation = str(data[0]) + " " + data[1] + " " + str(data[2])
            result = data[3]
            cursor.execute(f"INSERT INTO calculations (equation, result) VALUES ('{equation}', {result});")
            connection.commit()


def print_result(data):
    # print("{} {} {} = {}".format(val1, operation, val2, result))
    print(f"{data[0]} {data[1]} {data[2]} = {data[3]} | {data[4]}")  # New and better way
    return


def main():
    num1 = int(input("Please enter your first number: "))
    num2 = int(input("Please enter your second number: "))
    addition = (num1, "+", num2, calc_module.addition(val1=num1, val2=num2), "")
    print_result(addition)
    add_database(addition)
    subtraction = (num1, "-", num2, calc_module.subtraction(num1, num2), "")
    print_result(subtraction)
    add_database(subtraction)
    multiplication = (num1, "*", num2, calc_module.multiplication(num1, num2), "")
    print_result(multiplication)
    add_database(multiplication)
    # assert num1 != 0, "Sorry, number 1 should not be zero. (Using assert method)"
    division = (num1, "/", num2, calc_module.division_with_exception(num1, num2), "")
    print_result(division)
    add_database(division)
    return


if __name__ == "__main__":
    with closing(sqlite3.connect("data.db")) as connection:
        with closing(connection.cursor()) as cursor:
            cursor.execute("CREATE TABLE IF NOT EXISTS calculations (id INTEGER PRIMARY KEY, equation TEXT, result INTEGER);")
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()
            print("Existing tables in data.db")
            for item in tables:
                print(item)

    for i in range(0, 2):
        main()

    """with closing(sqlite3.connect("data.db")) as connection:
        with closing(connection.cursor()) as cursor:
            cursor.execute("SELECT * FROM calculations")
            records = cursor.fetchall()
            for record in records:
                print(record)"""
