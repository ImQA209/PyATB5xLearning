class grandfather:
    Bhk = "3BHK"

    def gf_car(self):
        print(self.Bhk)


class father(grandfather):
    gold = "15kg"

    def father_dp(self):
        print("gold")


class son(father):
    BTN = "200"

    def son_dp(self):
        print("BTN")


s = son()
print(s.BTN)
s.gf_car()
