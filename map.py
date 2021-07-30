import random
import io_helper as io

class Labyrinth(object):
    def __init__(self, level=0):
        self.level = level
        self.row_min = 0
        self.row_max = 10
        self.col_min = 0
        self.col_max = 10
        self.columns = self.col_max + level**2
        self.rows = self.row_max + level**2
        self.create_map()
        self.create_labyrinth((self.row_max//2, self.col_max//2))
        self.create_total_map()

    def create_map(self) -> list:
        self.map = dict()
        # komplett mit Wänden befüllt:
        for row in range(self.rows):
            for column in range(self.columns):
                pos = row, column
                self.map[pos] = Cell(row, column)
        
    def create_labyrinth(self, pos):
        cur_cell = self.map[pos]
        neighbors = self.get_non_visited_neighbors(pos)
        if len(neighbors) < 1:
            return
        neighbor = random.choice(neighbors)
        cur_cell.remove(neighbor[1])
        self.create_labyrinth(neighbor[0])

    def create_total_map(self) -> list:
        total_map = []
        for row in range(self.row_max):
            row_map_0 = []
            row_map_1 = []
            row_map_2 = []
            for col in range(self.col_max):
                cur_cell = self.map[(row, col)]
                row_map_1 += [int(cur_cell.up), int(cur_cell.up), int(cur_cell.up)]
                row_map_1 += [int(cur_cell.left), 0, int(cur_cell.right)]


    def reached_edge(self, pos) -> bool:
        if pos[0]-1 < self.row_min:
            return True
        elif pos[0]+1 > self.row_max:
             return True
        elif pos[1]-1 < self.col_min:
            return True
        elif pos[1]+1 > self.col_max:
            return True  
        else:
            return False  

    # man könnte zusätzlich prüfen, ob es eine Wand ist
    def get_neighbors(self, pos):
        neighbors = []
        if pos[0]-1 >= self.row_min:
            neighbors += [(pos[0]-1, pos[1])]
        if pos[0]+1 <= self.row_max:
             neighbors += [(pos[0]+1, pos[1])]
        if pos[1]-1 >= self.col_min:
            neighbors += [(pos[0], pos[1]-1)]
        if pos[1]+1 <= self.col_max:
            neighbors += [(pos[0], pos[1]+1)]
        return neighbors

    def get_non_visited_neighbors(self, pos):
        neighbors = []
        if pos[0]-1 >= self.row_min and not self.map[(pos[0]-1, pos[1])].visited:
            neighbors += [[(pos[0]-1, pos[1]), 'left']]
        if pos[0]+1 <= self.row_max and not self.map[(pos[0]+1, pos[1])].visited:
             neighbors += [[(pos[0]+1, pos[1]), 'right']]
        if pos[1]-1 >= self.col_min and not self.map[(pos[0], pos[1]-1)].visited:
            neighbors += [[(pos[0], pos[1]-1), 'up']]
        if pos[1]+1 <= self.col_max and not self.map[(pos[0], pos[1]+1)].visited:
            neighbors += [[(pos[0], pos[1]+1), 'down']]
        return neighbors

    def draw(self):
        io.print_with_only_delay(f"{io.CLEAR_SCREEN(2)}{io.SET_POSITION(0, 0)}", 0, 0)
        for row in range(self.row_max*3):    # links weg rechts
            for column in range(self.col_max*3):    # oben weg unten
                io.print_with_only_delay(f"{io.SET_POSITION(key[0], key[1]*2+1)}#", 0, 0)

    def update_pos(self, old_pos, new_pos):
        pass


class Cell(object):
    # True = Wall
    def __init__(self, row, column, visited=False, value=None, left=True, right=True, up=True, down=True):
        self.row = row
        self.column = column

        self.visited = visited    # for labyrinth creation

        self.value = value

        self.left = left
        self.right = right
        self.up = up
        self.down = down

    def get_pos(self) -> tuple:
        return (self.row, self.column)

    def get_value(self) -> any:
        return self.value

    def update_value(self, new_value):
        self.value = new_value

    def remove(self, direction:str):
        self.direction = not self.direction


# testing
if __name__ == '__main__':
    lbyr = Labyrinth()
    lbyr.draw()
