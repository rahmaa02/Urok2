from hard import factory, newGame


class Game:
    def __init__(self, name, color):
        self.name=name
        self.color=color

    def __str__(self):
        return f'game {self.name}, color {self.color}'

class Animal(Game):
    def __init__(self, name, color):
        super().__init__(name, color)

    def __str__(self):
        return f'Animal {self.name}, color {self.color}'


class Film(Game):
    def __init__(self, name, color):
        super().__init__(name, color)

    def __str__(self):
        return f'Film {self.name}, color {self.color}'


class Factory:
    def __init__(self,name, color, tip_game):
        self.name=name
        self.color=color
        self.tip_game=tip_game

    def закупка_сырья(self):
        print('Закупка сырья для игрушки')

    def пошив(self):
        print('Пошив игрушки')

    def окрас(self):
        print(f'Окрас игрушки в {self.color} цвет')

    def собрать_игрушку(self):
        self.закупка_сырья()
        self.пошив()
        self.окрас()

        if self.tip_game== 'Animal':
            return Animal(self.name, self.color)
        elif self.tip_game== 'Film':
            return Film(self.name, self.color)
        else:
            raise ValueError ('Error')

print('############################')

factory1 = Factory('Dog', 'серый', 'Animal')
game1= factory1.собрать_игрушку()
print(game1)

print('############################')

factory2 = Factory('Cat', 'Green', 'Film')
game2= factory2.собрать_игрушку()
print(game2)