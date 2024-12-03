a = 11


class Test_class:
    b = 11

    def Test_display(self):
        c = 15
        print(c)
        global a
        a = "hello"

        print(a)


ref1 = Test_class()
ref1.Test_display()
