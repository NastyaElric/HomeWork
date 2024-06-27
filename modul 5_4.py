class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args)
        object.__new__(cls)
        return object.__new__(cls)

    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def __del__(self):
        print(f" {self.name} снесён, но останется в итории")

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)