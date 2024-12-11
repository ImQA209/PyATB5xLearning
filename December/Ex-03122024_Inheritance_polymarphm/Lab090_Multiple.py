class Father:
    def FatherMoney(self):
        return 10


class Mother:
    def MotherMoney(self):
        return 15

    def home(self):
        return "This is mother money"


class son(Father, Mother):
    def son1(self):
        print("son")


s = son()
print(s.home())
s.son1()
