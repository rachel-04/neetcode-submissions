class SpiderMan:
    def attack(self) -> str:
        return "Web Shooter!"
    
    def defend(self) -> str:
        return "Spider Sense!"
class BlackWidow:
    def attack(self) -> str:
        return "Widow's Bite!"
    def defend(self) -> str:
        return "Acrobatic Dodge!"
# TODO: Create the BlackWidow class with attack() and defend() methods
def battle_sequence(object):
    print(object.attack())
    print(object.defend())


# TODO: Create the battle_sequence() function



# Don't modify the code below
spider_man = SpiderMan()
black_widow = BlackWidow()

battle_sequence(spider_man)
battle_sequence(black_widow)
