class Calculator:
    def add(self, a, b):
        """Return the sum of two numbers."""
        return a + b

    def subtract(self, a, b):
        """Return the difference between two numbers."""
        return a - b

    def multiply(self, a, b):
        """Return the product of two numbers."""
        return a * b

    def divide(self, a, b):
        """Return the division of two numbers."""
        if b == 0:
            return "Error: Division by zero"
        return a / b


cal = Calculator()
a = float(input("Enter the value of a:"))
b = float(input("Enter the value of b:"))

Addition = cal.add(a, b)
subtraction = cal.subtract(a, b)
multiplication = cal.multiply(a, b)

division = cal.divide(a, b)

print("The sum of two numbers:", + Addition)
print("The divison of two numbers:", + division)
