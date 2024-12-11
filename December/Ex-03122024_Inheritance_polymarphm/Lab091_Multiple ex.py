class a1:
    def method(self):
        return "a1 method"


class b1:
    def method(self):
        return "b1 method"


class c(b1, a1):
    def c1(self):
        pass


call = c()
print(call.method())
