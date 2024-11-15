a = int(input("Enter the side value1:"))
b = int(input("Enter the side value2:"))
c = int(input("Enter the side value3:"))
if a == b == c:
    print("This is: ", "Equilateral Triangle")
elif a == b or b == c or c == a:
    print("This is: ", "Isosceles Triangle")
else:
    print("This is: Scalene Triangle")
