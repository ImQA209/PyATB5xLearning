class Father:
    home = "1 BHK"
    car = "BMW"

    def display(self):  # Corrected method name
        print(self.home)
        print(self.car)


class Son(Father):
    home1 = "2 BHK"  # Added space for consistency
    car1 = "Ford"  # Corrected variable name for consistency

    def display1(self):
        print(self.home1)
        print(self.car1)


# Testing the classes
test = Father()
test.display()  # Call the parent class method

son_test = Son()
son_test.display()  # Call the inherited method
print("-------------------")
son_test.display1()  # Call the method defined in the child class
