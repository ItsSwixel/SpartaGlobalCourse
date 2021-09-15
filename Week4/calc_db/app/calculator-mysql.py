from calc_package import calc_module
import mysql.connector


def add_database(data):
    with mysql.connector.connect(host="localhost", user="root", password="my_secret_password", database="calculator") as conn:
        cursor = conn.cursor()
        equation = str(data[0]) + " " + data[1] + " " + str(data[2])
        result = data[3]
        cursor.execute(f"INSERT INTO calculations (equation, result) VALUES ('{equation}', {result});")
        conn.commit()


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
    try:
        with mysql.connector.connect(host="localhost", user="root", password="my_secret_password", database="calculator") as conn_var:
            cursor = conn_var.cursor()
            print("Database connection status: Successful")
    except Exception as err:
        with mysql.connector.connect(host="localhost", user="root", password="my_secret_password") as conn_var:
            cursor = conn_var.cursor()
            cursor.execute("CREATE DATABASE calculator")
            cursor.execute("USE calculator")
            cursor.execute("CREATE TABLE calculations (id INT AUTO_INCREMENT PRIMARY KEY, equation VARCHAR(20), result INT);")
            cursor.execute("SHOW TABLES;")
            print(cursor)
            for item in cursor:
                print(item)
    finally:
        for i in range(0, 2):
            main()
