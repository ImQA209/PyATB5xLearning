# Hide the data value
class car:

    def __init__(self):
        self.password = "Iyappan"
        self.__password_secure = "Iyappan123"

    def change_pwd(self):
        print(self.password)


obj_ref = car()
print(obj_ref.password)
print(obj_ref.change_pwd())
