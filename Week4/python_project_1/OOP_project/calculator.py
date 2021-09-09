class CalculatorClass:
    counter = 0

    @classmethod
    def update_counter(cls):
        cls.counter += 1

    @classmethod
    def get_counter(cls):
        return cls.counter

    def __init__(self, number1, number2):
        self.num1 = number1
        self.num2 = number2

    def add(self):
        self.update_counter()
        return self.num1 + self.num2

    def subtract(self):
        self.update_counter()
        return self.num1 - self.num2

    def multiply(self):
        self.update_counter()
        return self.num1 * self.num2

    def divide(self):
        self.update_counter()
        return self.num1 / self.num2
