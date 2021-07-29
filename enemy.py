import abc

class Enemy(abc.ABC):
    def __init__(self, name:str, health:int, attack_pool):
        self.name = name
        self.health = health
        self.attack_pool = attack_pool

    def attack(self):
        pass

    def get_damage(self):
        pass
