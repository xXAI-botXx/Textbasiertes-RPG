import random
import io_helper as io

class Maze(object):
    def __init__(self, level=0):
        self.level = level
        self.row_min = 0
        self.row_max = 10    # [min, max) -> max not included
        self.col_min = 0
        self.col_max = 10
        self.columns = self.col_max + level**2
        self.rows = self.row_max + level**2
        self.start_pos = (self.row_max//2, self.col_max//2)
        self.start_pos = (0, 0)
        self.create_map()
        self.create_maze(self.start_pos)
        self.create_total_map()

    def create_map(self) -> list:
        self.map = dict()
        self.not_marked = []
        self.visited = []
        # komplett mit Wänden befüllt:
        for row in range(self.rows):
            for column in range(self.columns):
                pos = row, column
                cur_cell = Cell(row, column)
                self.map[pos] = cur_cell
                self.not_marked += [cur_cell]
        
    def create_maze(self, pos):
        while True:
            if len(self.not_marked) < 1:
                break

            cur_cell = self.map[pos]
            cur_cell.visited = True
            self.not_marked.remove(cur_cell)
            self.visited += [cur_cell]

            neighbors = self.get_non_visited_neighbors(pos)
            if len(neighbors) < 1:
                other_neighbor = self.get_pos_with_not_marked_neighbor()
                if other_neighbor == None:
                    print("Upps here you shouldnt be...")
                    break
                #self.create_maze(other_neighbor)
                pos = other_neighbor
            else:
                neighbor = random.choices(neighbors, k=1)
                cur_cell.remove(neighbor[0][1])
                self.map[neighbor[0][0]].remove_opposite(neighbor[0][1])
                #self.create_maze(neighbor[0][0])
                pos = neighbor[0][0]

    def create_total_map_(self) -> list:
        total_map = []
        for row in range(self.row_max):
            row_map_0 = []
            row_map_1 = []
            row_map_2 = []
            for col in range(self.col_max):
                cur_cell = self.map[(row, col)]

                left_up = int(cur_cell.up)
                right_up = int(cur_cell.up)
                if int(cur_cell.left) == 1:
                    left_up = 1 
                if int(cur_cell.right) == 1:
                    right_up = 1
                row_map_0 += [left_up, int(cur_cell.up), right_up]
                row_map_1 += [int(cur_cell.left), 0, int(cur_cell.right)]
                left_down = int(cur_cell.up)
                right_down = int(cur_cell.up)
                if int(cur_cell.left) == 1:
                    left_down = 1 
                if int(cur_cell.right) == 1:
                    right_down = 1
                row_map_2 += [left_down, int(cur_cell.down), right_down]

            total_map += [row_map_0]
            total_map += [row_map_1]
            total_map += [row_map_2]
        self.total_map = total_map

    
    def create_total_map(self) -> list:
        total_map = []
        for row in range(self.row_max):
            row_map_0 = []
            row_map_1 = []
            row_map_2 = []
            for col in range(self.col_max):
                cur_cell = self.map[(row, col)]

                left_up = int(cur_cell.up)
                right_up = int(cur_cell.up)
                row_map_0 += [left_up, int(cur_cell.up), right_up]
                row_map_1 += [int(cur_cell.left), 0, int(cur_cell.right)]
                left_down = int(cur_cell.up)
                right_down = int(cur_cell.up)
                row_map_2 += [left_down, int(cur_cell.down), right_down]

            total_map += [row_map_0]
            total_map += [row_map_1]
            total_map += [row_map_2]
        self.total_map = total_map

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
        if pos[0]+1 < self.row_max:
             neighbors += [(pos[0]+1, pos[1])]
        if pos[1]-1 >= self.col_min:
            neighbors += [(pos[0], pos[1]-1)]
        if pos[1]+1 < self.col_max:
            neighbors += [(pos[0], pos[1]+1)]
        return neighbors

    def get_non_visited_neighbors(self, pos):
        neighbors = []
        if pos[0]-1 >= self.row_min:
            if not self.map[(pos[0]-1, pos[1])].visited:
                neighbors += [[(pos[0]-1, pos[1]), 'left']]
        if pos[0]+1 < self.row_max:
            if not self.map[(pos[0]+1, pos[1])].visited:
                neighbors += [[(pos[0]+1, pos[1]), 'right']]
        if pos[1]-1 >= self.col_min:
            if not self.map[(pos[0], pos[1]-1)].visited:
                neighbors += [[(pos[0], pos[1]-1), 'up']]
        if pos[1]+1 < self.col_max:
            if not self.map[(pos[0], pos[1]+1)].visited:
                neighbors += [[(pos[0], pos[1]+1), 'down']]
        return neighbors

    def get_pos_with_not_marked_neighbor(self):
        visited_cells = self.visited.copy()
        visited_cells.reverse()
        for visited_cell in visited_cells:
            result = self.get_non_visited_neighbors(visited_cell.get_pos())
            if len(result) > 0:
                return random.choices(result, k=1)[0][0]
        return None

    def get_pos_with_not_marked_neighbor_alt(self):
        unused_visited_cells = self.visited.copy()
        while True:
            if len(unused_visited_cells) < 1:
                break
            visited_cell = random.choices(unused_visited_cells, k=1)[0]
            result = self.get_non_visited_neighbors(visited_cell.get_pos())
            if len(result) > 0:
                return random.choices(result, k=1)[0][0]
            else:
                unused_visited_cells.remove(visited_cell)
        return None

    def draw(self):
        io.print_with_only_delay(f"{io.CLEAR_SCREEN(2)}{io.SET_POSITION(0, 0)}", 0, 0)
        for row in range(self.row_max*3):    # links weg rechts
            for column in range(self.col_max*3):    # oben weg unten
                cur_pos = self.total_map[row][column]
                if cur_pos == 0:
                    io.print_with_only_delay("  ", 0, 0)
                else:
                    io.print_with_only_delay(" #", 0, 0)
            io.print_with_only_delay("\n", 0, 0)

    def draw_with_pygame(self):
        import pygame
        pygame.init()
        tile_size = 50
        screen = pygame.display.set_mode((self.row_max*tile_size, self.col_max*tile_size))
        pygame.display.set_caption("Maze Generation Test")
        clock = pygame.time.Clock()

        r = pygame.Rect(self.start_pos[0]*tile_size+tile_size//4, self.start_pos[1]*tile_size+tile_size//4, tile_size-tile_size//2, tile_size-tile_size//2)
        pygame.draw.rect(screen, (150, 250, 150), r)

        for row in range(self.row_max):
            for col in range(self.col_max):
                cur_cell = self.map[(row, col)]
                x = row*tile_size
                y = col*tile_size
                # grid
                pygame.draw.line(screen, (50, 50, 50), [x, y], [x+tile_size, y])
                pygame.draw.line(screen, (50, 50, 50), [x, y+tile_size], [x+tile_size, y+tile_size])
                pygame.draw.line(screen, (50, 50, 50), [x, y], [x, y+tile_size])
                pygame.draw.line(screen, (50, 50, 50), [x+tile_size, y], [x+tile_size, y+tile_size])
                # walls
                if cur_cell.up:
                    pygame.draw.line(screen, (255, 255, 255), [x, y], [x+tile_size, y])
                if cur_cell.down:
                    pygame.draw.line(screen, (255, 255, 255), [x, y+tile_size], [x+tile_size, y+tile_size])
                if cur_cell.left:
                    pygame.draw.line(screen, (255, 255, 255), [x, y], [x, y+tile_size])
                if cur_cell.left:
                    pygame.draw.line(screen, (255, 255, 0), [x+tile_size, y], [x+tile_size, y+tile_size])
        
        pygame.display.update()
        running = True
        while running:
            clock.tick(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

    def print_map(self):
        for row in self.total_map:
            io.print_with_only_delay(str(row)+"\n", 0, 0)

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
        #eval(f"self.{direction} = not self.{direction}")
        if direction == "left":
            self.left = False
        elif direction == "right":
            self.right = False
        elif direction == "up":
            self.up = False
        elif direction == "down":
            self.down = False

    def remove_opposite(self, direction:str):
        #eval(f"self.{direction} = not self.{direction}")
        if direction == "left":
            self.right = False
        elif direction == "right":
            self.left = False
        elif direction == "up":
            self.down = False
        elif direction == "down":
            self.up = False


# testing
if __name__ == '__main__':
    maze = Maze()
    #maze.draw()
    #maze.print_map()
    maze.draw_with_pygame()
