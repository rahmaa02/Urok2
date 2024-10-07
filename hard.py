class Game:
    def __init__(self, name, color, tip_game):
        self.name=name
        self.color=color
        self.tip_game=tip_game

    def __str__(self):
        return f'game {self.name}, color {self.color}, tip_game {self.tip_game}'

class Factory:
    def __init__(self,name, color, tip_game):
        self.name=name
        self.color=color
        self.tip_game=tip_game

    def purchase(self):
        print('Закупка сырья для игрушки')

    def sewing(self):
        print('Пошив игрушки')

    def colouration(self):
        print(f'Окрас игрушки в {self.color} цвет')

    def assembling(self):
        self.purchase()
        self.sewing()
        self.colouration()
        newGame=Game(self.name, self.color, self.tip_game)
        return newGame

farcotyGame=Factory('Волк', 'серый', 'животное')
newGame=farcotyGame.assembling()
print(newGame)