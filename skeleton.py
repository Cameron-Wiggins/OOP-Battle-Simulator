import random
from enemy import Enemy

class Skeleton(Enemy):
    """
    This is our goblin blueprint 
    
    Attributes:
        name: Awe, it has a name? How cute!
        health: The current health value 
        attack_power: How much health will be drained from opponent if hit
    """
    def __init__(self, color, name):
        super().__init__
        self.health= 25
        self.color=color
        self.name=name
        self.attack_power= random.randint(10,20)

    def attack(self):
        return self.attack_power
