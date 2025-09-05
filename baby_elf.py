from enemy import Enemy

class BabyElf(Enemy):
    def take_damage(self, damage):
        self.health -= damage
        print("You Just Hit A Baby! How Could You!")