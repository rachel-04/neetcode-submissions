class SuperHero:
    def __init__(self, name: str, __health: int, __power_level: int):
        self.name = name
        self.__health = __health
        self.__power_level = __power_level
    
    
    def get_health(self)->int:
        return self.__health
    def get_power_level(self)->int:
        return self.__power_level
    
    def set_health(self, __health)-> None:
        if(0<=__health<=100):
            self.__health = __health
        elif(__health > 100):
            print("You can't set the health to more than 100")
        elif(__health <0):
            print("You can't set the health to less than 0")
    
    def set_power_level(self, __power_level)-> None:
        if(1<=__power_level<=10):
            self.__power_level = __power_level
        elif(__power_level > 10):
            print("You can't set the power level to more than 10")
        elif(__power_level <1):
            print("You can't set the power level to less than 1")

        



super_hero = SuperHero("Batman", 80, 9)

print(super_hero.get_health()) # this should print 80
super_hero.set_health(110) # this should print You can't set the health to more than 100
super_hero.set_health(-10) # this should print You can't set the health to less than 100
super_hero.set_health(70)

print(super_hero.get_power_level()) # this should print 9
super_hero.set_power_level(11) # this should print You can't set the power level to more than 10
super_hero.set_power_level(0) # this should print You can't set the power level to less than 1
super_hero.set_power_level(7)


print(f"{super_hero.name} has {super_hero.get_health()} health and {super_hero.get_power_level()} power level")
