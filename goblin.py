import random
from enemy import Enemy

class Goblin(Enemy):
    """
    This is our goblin blueprint 
    
    Attributes:
        name: Awe, it has a name? How cute!
        health: The current health value 
        attack_power: How much health will be drained from opponent if hit
    """
    def __init__(self, name, color):
        super().__init__
        self.health= 75
        self.color=color
        self.attack_power= random.randint(1,5)

    def attack(self):
        return self.attack_power
