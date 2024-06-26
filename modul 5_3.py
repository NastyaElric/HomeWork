class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.buildingType = buildingType
        self.numberOfFloors = numberOfFloors

    def __eq__(self, other):
        return self.buildingType == other.buildingType and self.numberOfFloors == other.numberOfFloors

house = Building(5, "Дом")
house2 = Building(17, "Многоэтажка")
print(house == house2)

