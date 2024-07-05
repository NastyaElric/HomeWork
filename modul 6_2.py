class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    def __init__(self, name, __model, __color, __engine_power):
        self.name = name
        self.__model = __model
        self.__color = __color
        self.__engine_power = __engine_power

    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Вдаделец: ", self.name)





class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def set_color(self, new_color):

        self.new_color = new_color
        for i in self._Vehicle__COLOR_VARIANTS:
            new_color_u = i.upper()
            if new_color in new_color_u:
                self._Vehicle__color = new_color
            else:
                continue
            if new_color not in self._Vehicle__COLOR_VARIANTS:
                print("В такой цвет покрасить нельзя")




vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
vehicle1.print_info()
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.name = 'Vasyok'
vehicle1.print_info()
