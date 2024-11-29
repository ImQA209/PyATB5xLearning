# Create a Class PyATB , 5 Attributes, 3 Functions/Methods
class pyATB:
    Name = None
    Age = None
    exp = None
    company = None
    dept = None

    def __init__(self, Name, Age, exp, company, dept):
        self.Name = Name
        self.age = Age
        self.exp = exp
        self.company = company
        self.dept = dept

    def Student_info(self):
        print(f"Student Name: {self.Name}", f"Age is: {self.age}", f"experience is: {self.exp}",
              f"Company is: {self.company}",
              f"Department is: {self.dept}")


s1 = pyATB("Iyappan", 33, 7, "zeesoft", "QA")
s2 = pyATB("Test", 30, 5, "tcs", "php")
s3 = pyATB("vibin", 26, 5, "ust", "java")

s1.Student_info()
s2.Student_info()
s3.Student_info()
