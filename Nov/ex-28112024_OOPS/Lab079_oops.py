class dog:
    name = "none"
    bride = "none"
    age = "none"

    def __init__(self, name, age):
        print("pc")
        self.name = name
        self.age = age

    def sleep(self):
        print("sleeping")

    def bark(self):
        print("bark")

    def walk(self):
        print("walking")


d1_ref = dog("test", 1)
d2_ref = dog("zee", 2)
print(d1_ref.age)
print(d2_ref.name)
