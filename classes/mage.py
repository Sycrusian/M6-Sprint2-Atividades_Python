from .villager import Villager


class Mage(Villager):

    def __init__(self, name: str):
        super().__init__(name)
        self.attack = 10
        self.mana = 100

    def fire_ball(self, target):
        if (self.mana < 20):
            return "Not enough mana!"
        self.mana -= 20
        return target.check_health(self.attack + 20)
