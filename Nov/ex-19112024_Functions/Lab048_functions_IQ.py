# create a program for sum of three number
#If user didnot enter any number use default value of 100,20,50

num1=int(input("Enter the number1:"))
num2=int(input("Enter the number2:"))
num3=int(input("Enter the number3:"))

def sum_of_num(n1=100,n2=20,n3=50):
    return n1+n2+n3
result=sum_of_num(num1,num2,num3)
print(result)

result2=sum_of_num()
print("The default value:",result2)


