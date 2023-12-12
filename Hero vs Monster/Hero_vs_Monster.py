class Hero:
    def __init__(self, weapon_damage, health, healing_potion=False):
        self.weapon_damage = weapon_damage
        self.health = health
        self.healing_potion = healing_potion

    def attack(self, monster):
        monster.health -= self.weapon_damage
        print(f"You attack the monster with your weapon and deal {self.weapon_damage} damage.")

    def take_damage(self, damage):
        self.health -= damage
        print(f"The monster attacks you for {damage} damage.")

    def drink_potion(self):
        if self.healing_potion:
            self.healing_potion = False
            self.health += 5
            print("You drink the healing potion and regain 5 health.")
        else:
            print("You don't have any healing potions left.")

    def is_alive(self):
        return self.health > 0

class Monster:
    def __init__(self, attack_strength, health):
        self.attack_strength = attack_strength
        self.health = health

    def roar(self):
        print("The monster roars!")

    def attack(self, hero):
        hero.take_damage(self.attack_strength)
        print(f"The monster attacks you for {self.attack_strength} damage.")

    def take_damage(self, damage):
        self.health -= damage
        print(f"You attack the monster and deal {damage} damage.")

    def run_away(self):
        print("The monster runs away!")

    def is_alive(self):
        return self.health > 0

# Create custom Hero and Monster
desired_weapon_damage = int(input("What weapon damage do you want for your hero? "))
desired_hero_health = int(input("What starting health do you want for your hero? "))
hero = Hero(desired_weapon_damage, desired_hero_health)

desired_monster_attack = int(input("What attack strength do you want for the monster? "))
desired_monster_health = int(input("What starting health do you want for the monster? "))
monster = Monster(desired_monster_attack, desired_monster_health)

# Start the game loop
while hero.is_alive() and monster.is_alive():
    # Get user input
    action = input("What do you want to do? (attack, drink, info) ")

    # Perform action based on user input
    if action == "attack":
        hero.attack(monster)
    elif action == "drink":
        hero.drink_potion()
    elif action == "info":
        print(f"Hero health: {hero.health}")
        print(f"Monster health: {monster.health}")
    else:
        print("Invalid action.")

    # Check if monster is alive and can fight back
    if monster.is_alive():
        monster.attack(hero)

    # Check if monster has to run away
    if monster.health == 1:
        monster.run_away()

# Game over message
if hero.is_alive():
    print("Congratulations! You defeated the monster!")
else:
    print("Game over! You were defeated by the monster.")

