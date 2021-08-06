class Animal:
    def __init__(self, life_time, weight):
        self.weight = weight
        self.life_time = life_time
        self.food = 3
        self.name = ''

    def get_food(self, food):
        self.food += food.weight

    def next_day(self):
        self.food -= 1
        if self.food <= 0:
            print(f'die {self.name}')


class Cat(Animal):

    def __init__(self, weight, color):
        super().__init__(10, weight)
        self.color = color
        self.name = 'cat '+color

    def get_food(self, food):
        super().get_food(food)
        print("mau mau")

class Dog(Animal):

    def __init__(self, weight, color):
        super().__init__(20, weight)
        self.color = color
        self.name = 'dog'

if __name__ == '__main__':
    cat_blue = Cat(20, 'blue')
    cat_red = Cat(50, 'red')
    dog = Dog(10, 'black')
    animals = [cat_blue, cat_red, dog]

    day = 0

    def run_day():
        print('next day')
        for animal in animals:
            animal.next_day()

    run_day()
    cat_red.get_food(Animal(life_time=2, weight=12))
    run_day()
    run_day()