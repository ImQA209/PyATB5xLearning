class Car:
    def __init__(self, o_name, o_model, o_engine):
        self.name = o_name
        self.model = o_model
        self.engine = o_engine

    def start_engine(self):
        print("starting car with name: " + self.name)
        print("starting car with model: " + self.model)
        print("starting car with engine: " + self.engine)


lambo = Car("lambo", "2023", "v6")
lambo.start_engine()
print("---------------------- ---------------------")
swift = Car("dezire", "2024", "quroject")
swift.start_engine()
