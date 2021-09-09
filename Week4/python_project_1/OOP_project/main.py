import calculator

for i in range(0,2):
    num1 = int(input("Please enter your first number: "))
    num2 = int(input("Please enter your second number: "))

    calcObject = calculator.CalculatorClass(num1, num2)
    sum = calcObject.add()
    print(f"{num1} + {num2} = {sum}")
    print(f"Total operations = {calcObject.get_counter()}")

    sub = calcObject.subtract()
    print(f"{num1} - {num2} = {sub}")
    print(f"Total operations = {calcObject.get_counter()}")

    mul = calcObject.multiply()
    print(f"{num1} * {num2} = {mul}")
    print(f"Total operations = {calcObject.get_counter()}")

    div = calcObject.divide()
    print(f"{num1} / {num2} = {div}")
    print(f"Total operations = {calcObject.get_counter()}")