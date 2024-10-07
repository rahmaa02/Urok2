from pydoc import plain


class Person:
    def __init__(self, health, damage, armor):
        self.health=health
        self.damage=damage
        self.armor=armor

    def __calculate_damage(self, damage):
        return max(0, damage - self.armor)

    def attack(self, opponent):
        damage_dealt = self.__calculate_damage(self.damage)
        opponent.health -= damage_dealt
        print(f"{self.__class__.__name__} атаковал {opponent.__class__.__name__} на {damage_dealt} урона!")
        print(f"Здоровье {opponent.__class__.__name__}: {opponent.health}")

class Player(Person):
    def __init__(self, health=100, damage=20, armor=5):
        super().__init__(health, damage, armor)

class Enemy(Person):
    def __init__(self, health=80, damage=15, armor=3):
        super().__init__(health, damage, armor)

class Game:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def start(self):
        while self.player.health > 0 and self.enemy.health > 0:
            self.player.attack(self.enemy)
            if self.enemy.health <= 0:
                print('Игрок победил!')
                break
            self.enemy.attack(self.player)
            if self.player.health <= 0:
                print('Враг победил!')
                break
player=Player()
enemy=Enemy()
game = Game(player, enemy)
game.start()