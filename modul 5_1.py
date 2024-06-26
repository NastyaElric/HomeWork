class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, floor):
        if floor < 1 or floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            for i in range(1, self.number_of_floors):
                if i <= floor:
                    print(i)
                    continue
                else:
                    break


h1 = House('ЖК Горский', 10)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(18)



