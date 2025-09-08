import random
from goblin import Goblin
from hero import Hero
from skeleton import Skeleton
from boss import Brute


def main():
    print("Welcome to the Battle Arena!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")

    # Create a hero
    hero = Hero("Terry")

    # Create goblins ༼ ºل͟º ༽ ༼ ºل͟º ༽ ༼ ºل͟º ༽
    goblins = [Goblin(f"Goblin {i+1}" , "Green") for i in range(random.randint(2,5))]

    # Create skeletons
    skeltons = [Skeleton(f"Skelton {i+1}" , "White") for i in range(random.randint(1,3))]


    # Keep track of how many goblins were defeated
    defeated_goblins = 0
    defeated_skeltons = 0
    total_damage_ofgoblin = 0
    total_damage_ofhero = 0
    total_rounds = 0

    # Battle Loop 
    while hero.is_alive() and any(goblin.is_alive() for goblin in goblins):
        print("\nNew Round!")
        total_rounds = total_rounds + 1
        
        # Hero's turn to attack goblin
        target_goblin = random.choice([goblin for goblin in goblins if goblin.is_alive()])
        damage = hero.strike()
        print(f"Hero attacks {target_goblin.name} for {damage} damage!")
        target_goblin.take_damage(damage)
        total_damage_ofhero = total_damage_ofhero + damage

        # Hero's turn to attack skelton
        target_skeltons = random.choice([skeltons for skeltons in skeltons if skeltons.is_alive()])
        damage = hero.strike()
        print(f"Hero attacks {target_skeltons.name} for {damage} damage!")
        target_skeltons.take_damage(damage)
        total_damage_ofhero = total_damage_ofhero + damage


        # Check if the target goblin was defeated
        if not target_goblin.is_alive():
            defeated_goblins = defeated_goblins + 1
            print(f"{target_goblin.name} has been defeated!")

        # Check if the target skeleton was defeated
        if not target_skeltons.is_alive():
            defeated_skeltons = defeated_skeltons + 1
            print(f"{target_skeltons.name} has been defeated!")


        # skeleton' turn to attack
        for skeltons in skeltons:
            if goblin.is_alive():
                damage = goblin.attack()
                print(f"{goblin.name} attacks hero for {damage} damage!")
                hero.receive_damage(damage)
                total_damage_ofgoblin = total_damage_ofgoblin + damage
        
        
        # skeleton' turn to attack
        for goblin in goblins:
            if goblin.is_alive():
                damage = goblin.attack()
                print(f"{goblin.name} attacks hero for {damage} damage!")
                hero.receive_damage(damage)
                total_damage_ofgoblin = total_damage_ofgoblin + damage


    # Determine outcome
    if hero.is_alive():
        print(f"\nThe hero has defeated all the goblins! ༼ ᕤ◕◡◕ ༽ᕤ")
        print(f"total damage was: {total_damage_ofgoblin + total_damage_ofhero}")
        print(f"total rounds was: {total_rounds}")
        # Final tally of goblins defeated
        print(f"Total goblins defeated: {defeated_goblins}")        

    else:
        print(f"\nThe hero has been defeated. Game Over. (｡•́︿•̀｡)")
        print(f"total damage was: {total_damage_ofgoblin + total_damage_ofhero}")
        print(f"total rounds was: {total_rounds}")
        # Final tally of goblins defeated
        print(f"Total goblins defeated: {defeated_goblins}")
    
    if hero.is_alive():
        print("boss fight time!")
        brute = Brute("Doug")
        while hero.is_alive() and brute.is_alive():
            damage = hero.strike()
            brute.take_damage(damage)
            damage= brute.strike()
            hero.receive_damage(damage)
        
        if hero.is_alive():
            print("You defeated the Boss!")
        else:
            print("You have been defeated by the Boss. (｡•́︿•̀｡) ")



if __name__ == "__main__":
    main()
