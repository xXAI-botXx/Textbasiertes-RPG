

class Player(object):

    SKILLS = [['Feuerball'], []]

    def __init__(self, health=10, stamina=10, magic=10, skills=[], skill_tree=[0, 0, 0, 0], skill_points=0, inventory=[], equipment=[]):
        self.health = health
        self.stamina = stamina
        self.magic = magic
        self.skills = skills
        self.skill_tree = skill_tree
        self.skill_points = skill_points
        self.inventory = inventory
        self.equipment = equipment

    def get_move(self):
        # solange bis Spieler Zug mit Bewegungskosten tätigt
        while True:
            pass

    def level_up(self):
        pass

    def skill_tree(self):
        pass
