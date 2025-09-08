import random
from enemy import Enemy

class Brute(Enemy):
    

    def __init__(self, name):
        super().__init__(name)
        self.attack_power = 10
        self.health=250

    def strike(self):
        # TODO Implement the hero's attack logic. It could be stronger or more consistent than a goblin's.
        return random.randint(3, self.attack_power)


    def attack(self):
        if self.health < 200:
            self.attack_power = 20
        elif self.health < 150:
            self.attack_power = 30
        elif self.health < 100:
            self.attack_power = 40
        elif self.health < 50:
            self.attack_power = 50