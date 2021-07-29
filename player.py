

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

        self.move_commands = {'schauen':self.look, 'rechts drehen':self.rotate_right, 'links drehen':self.rotate_left, 'inventar':self.open_inventory, 
                              'angriff':self.attack, 'verteidigen':self.defend, 'ausrüstung':self.open_equipment, 'magie':self.open_magic}

    def get_move(self):
        # solange bis Spieler Zug mit Bewegungskosten tätigt
        while True:
            pass

    def look(self):
        pass

    def rotate_right(self):
        pass

    def rotate_left(self):
        pass

    def open_inventory(self):
        pass

    def attack(self):
        # Angriff mit der primären Waffe -> Das ist standard, weitere Angriffe sind im Inventarmenü und im magiemenü verfügbar
        pass

    def defend(self):
        # Verteidigung mit Schild oder nichts
        pass

    # gibt es Ausrüstungsabteil, oder ist das im Inventar einfach eingebaut?
    def open_equipment(self):
        pass

    def open_magic(self):
        # wie erhält man Spells? -> durch Items -> Bücher oder durch Skillsystem? -> später klären
        pass

    def level_up(self):
        pass

    def skill_tree(self):
        pass
