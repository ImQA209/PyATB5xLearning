from sys import exception

print("----Start the program---")

try:
    a = int(input("Enter the num1:"))
    b = int(input("Enter the num2:"))
    result = a / b

except ValueError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)

else:
    print("The div result:", result)

print("---End of the program----")
