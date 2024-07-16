class Product():
    def __init__(self, name, wight, category):
        self.name = name
        self.wight = wight
        self.category = category

    def __str__(self):
        return f"{self.name} - {self.wight} кг, {self.category}"

class Shop():
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        __file_name = 'products.txt'
        file = open(self.__file_name, "r")
        return file.read()
        file.close()

    def add(self, *product):
        __file_name = 'products.txt'
        for p in product:
            if p not in product:
                file = open(self.__file_name, "w")
                file.write(p)
            else:
                print(f"Продукт {p.name} уже есть в магазине")



s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())