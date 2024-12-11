class parent:
    gold = "2kg"

    def parent_display(self):
        print(self.gold)
        print("Alto", "2024")


class child(parent):
    diamond = "4kg"

    def child_display(self):
        print(self.diamond)


test_ref = child()
# test_ref.parent_display()
print(test_ref.gold)
print(test_ref.diamond)
