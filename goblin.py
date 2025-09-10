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
    def __init__(self, color, name):
        super().__init__
        self.health= 50
        self.color=color
        self.name=name
        self.attack_power= random.randint(5,10)
    def __str__(self):
        return f"{self.name} ({self.color})"

    def attack(self):
        return self.attack_power
