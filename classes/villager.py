class Villager:

    def __init__(self, name: str):
        self.name = name
        self.health = 50
        self.defense = 0
        self.attack = 0
        self.is_alive = True

    def check_health(self, incoming_attack_value: int):
        effective_attack_value = incoming_attack_value - self.defense
        if effective_attack_value <= 0:
            return self.health
        self.health -= effective_attack_value
        if self.health <= 0:
            self.health = 0
            self.is_alive = False
            return (False, "Target is dead!")
        return self.health

    def normal_attack(self, target):
        return target.check_health(self.attack)
