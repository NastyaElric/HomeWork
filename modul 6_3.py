class Horse:
    x_distance = 0
    sound = "Frrr"

    def __init__(self, x_distance, sound):

        self.x_distance = x_distance
        self.sound = sound
        super().__init__(Eagle)

    def run(self, dx):
        x_distance = self.x_distance + dx

class Eagle:

    y_distance = 0
    sound = 'I train, eat, sleep, and repeat'

    def __init__(self, y_distance, sound):
        self.y_distance = y_distance
        self.sound = sound
        super().__init__(Horse)

    def fly(self, dy):
        y_distance = self.y_distance + dy

class Pegasus(Horse, Eagle):

    def __init__(self, x_distance, y_distance, sound):
        super().__init__(x_distance, sound)
        super().__init__(y_distance, sound)


    def move(self, dx, dy):
        super().run()


    def get_pos(self):
        # super().x_distance()
        # super().y_distance()
        return self.x_distance, self.y_distance

    def voice(self):
        res = super().sound()
        print(res)

p1 = Pegasus(0,0, " ")

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
