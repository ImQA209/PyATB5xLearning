class person:
    def __init__(self):
        print("I will be called")
        self.name = input("enter the Name:")
        self.age = input("Enter the age:")
        self.phoneno = input("Enter the phoneno:")

    def display(self):
        print(f"Name is: {self.name}", f"Phoneno is: {self.phoneno}", f"age is: {self.age}")


person1 = person()
person1.display()
