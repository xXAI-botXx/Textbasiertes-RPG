import abc
import random

class Enemy(abc.ABC):
    def __init__(self, name:str, health:int, attack_pool, pos:tuple):
        self.name = name
        self.health = health
        self.attack_pool = attack_pool
        self.pos = pos
        self.alive = True

    @abc.abstractmethod
    def attack(self):
        if self.alive:
            pass

    @abc.abstractmethod
    def turn(self):
        if self.alive:
            pass    

    def get_damage(self, damage:int):
        self.health -= damage
        if self.health <= 0:
            self.alive = False

    def set_map(self, maze):
        self.maze = maze

    def set_pos(self, new_pos:tuple):
        self.pos = new_pos

class Demon(Enemy):
    def __init__(self, pos):
        attack_pool = {'default':self.attack, 'scratch':self.scratch}
        health = random.randint(5, 15)
        super().__init__(self, 'Demon', health, attack_pool, pos)

    def turn(self):
        if self.alive:
            # wenn kein Gegner vorne dran ist:
            # bewege dich eins weiter
            pass 

    def attack(self):
        if self.alive:
            return 2

    def scratch(self):
        if self.alive:
            return 3
