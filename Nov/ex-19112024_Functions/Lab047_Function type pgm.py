# No return type parameter/argument
def im():
    print("hello")


im()

#No return type with argument
def im1(name):
    print("Welcome",name)

im1("iyappan")

# No return type with default argument

def cs1(name="Iyappanmani"):
    print("Hello",name.upper())
cs1("Manivannan")
cs1()

#multiple arguments
def test( name1="zeesoft",name2="chennai"):
    print("company ->",name1,name2)
test(name1="Iyappan",name2="Delhi")
test()

# Argument with return type

def sum_of_two_num(a,b):
    return a+b
result= sum_of_two_num(10,50)
print("The sum value is:",result)