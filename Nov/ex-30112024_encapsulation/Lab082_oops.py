class person:
    def __init__(self, name):
        self.name = name

    def person_walk(self):
        return self.name


amit = person("amit")
pramod = person("Pramod")

print("who is walking:", amit.person_walk())
print("who ia WALKIng", pramod.person_walk())
