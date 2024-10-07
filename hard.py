class game:
    def __init__(self, name, color, tip_game):
        self.name=name
        self.color=color
        self.tip_game=tip_game

    def __str__(self):
        return f'game {self.name}, color {self.color}, tip_game {self.tip_game}'

class factory:
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
        newGame=game(self.name, self.color, self.tip_game)
        return newGame

farcotyGame=factory('Волк', 'серый', 'животное')
newGame=farcotyGame.собрать_игрушку()
print(newGame)