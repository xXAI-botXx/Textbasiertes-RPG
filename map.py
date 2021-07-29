import random

class Labyrinth(object):
    def __init__(self, level=0):
        self.level = level
        self.labyrinth = self.create_labyrinth()

    def create_labyrinth(self) -> list:
        pass

    def update_pos(self, old_pos, new_pos):
        pass
