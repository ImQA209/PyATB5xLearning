from sys import exception

print("----Start the program---")

try:
    a = int(input("Enter the num1:"))
    b = int(input("Enter the num2:"))
    result = a / b
    print("The div result:", result)

except Exception as e:
    print(e)

print("---End of the program----")
