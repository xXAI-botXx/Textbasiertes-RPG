import abc

class Enemy(abc.ABC):
    def __init__(self, name:str, health:int, attack_pool):
        self.name = name
        self.health = health
        self.attack_pool = attack_pool
        self.alive = True

    @abc.abstractmethod
    def attack(self):
        if self.alive:
            pass

    def get_damage(self, damage:int):
        self.health -= damage
        if self.health <= 0:
            self.alive = False

    def set_map(self, maze):
        self.maze = maze

class Demon(Enemy):
    def __init__(self, name:str, health:int, attack_pool):
        super().__init__(name, health, attack_pool)

    def attack(self):
        if self.alive:
            return 5
