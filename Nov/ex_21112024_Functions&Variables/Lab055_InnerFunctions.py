def outer_functions():
    var1 = 30
    
    def inner_function1():
        print(var1)

    def inner_function2():
        print(var1)

    inner_function1()
    inner_function2()


outer_functions()
print(outer_functions())
