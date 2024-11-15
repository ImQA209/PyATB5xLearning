num1 = int(input("enter the value\n"))
num2 = int(input("enter the value of num2\n"))
num3 = int(input("enter the value of num3\n"))

if num1 > num2 and num1 > num3:
    print("The biggest number is num1", num1)
elif num2 > num1 and num2 > num3:
    print("The biggest number is num2", num2)
else:
    print("The biggest number is num3", num3)
 