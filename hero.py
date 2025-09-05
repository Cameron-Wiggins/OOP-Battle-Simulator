import random
class Hero:
    """
    This is our hero blueprint.
    
    O=('-'Q)

    Attributes:
        name: The name of our adventurer.
        hp: The current health value.
        strength: The amount of damage the hero can deal.
        (Bonus) defence: A hero's ability to reduce incoming damage.
        (Bonus) special_ability: A unique ability the hero can use.
    """
    
    def __init__(self, name):
        #TODO Set the hero's name.
        self.name=name
        #TODO Set the hero's health. You might give the hero more health than a goblin.
        self.health=(350)
        #TODO Set the hero's attack power. Should it be more consistent than the goblin's?
        self.attack_power= random.randint(5, 10)
    

    def strike(self):
        # TODO Implement the hero's attack logic. It could be stronger or more consistent than a goblin's.
        return random.randint(3, self.attack_power)
    
    def receive_damage(self, damage):
        self.health -= damage
        reducechance = random.randint(1,10)
        if reducechance < 8:
            print (f"{self.name} hit a parry and only took {damage/2}. Health is now {self.health}.")
        # TODO Implement take_damage
        else: print(f"{self.name} takes {damage} damage. Health is now {self.health}.")
      
        # TODO We should prevent health from going into the NEGATIVE


    def is_alive(self):
    #TODO define is_alive      
        if self.health < 50:
            amulet = random.randint(1, 10)  
            if amulet == 1:
                self.health = self.health + 25
                print (f"A Goblin Dropped an Amulet and You Used it to gain 25 health. Health is now {self.health}.")
            
        return self.health > 0