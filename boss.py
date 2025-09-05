from enemy import Enemy

class Brute(Enemy):
    

    def __init__(self, name):
        super().__init__(name)
        self.attack_power = 30
        self.health=250


    def attack(self):
        if self.health < 200:
            self.attack_power = 40
        elif self.health < 150:
            self.attack_power = 50
        elif self.health < 100:
            self.attack_power = 70
        elif self.health < 50:
            self.attack_power = 90