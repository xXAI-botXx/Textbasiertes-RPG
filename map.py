# Source: https://en.wikipedia.org/wiki/Maze_generation_algorithm
# -> (Iterative) Randomized depth-first search

import random
import io_helper as io

class Maze(object):
    def __init__(self, level=0, debug=False, col_max=10, row_max=10):
        self.level = level
        self.row_min = 0
        self.row_max = row_max    # [min, max) -> max not included
        self.col_min = 0
        self.col_max = col_max
        self.columns = self.col_max + level**2
        self.rows = self.row_max + level**2
        self.start_pos = (self.row_max//2, self.col_max//2)
        self.cur_pos = self.start_pos
        #self.start_pos = (0, 0)
        self.create_map()
        if debug:
            self.pos = self.start_pos
            #self.debug_create_maze()
        else:
            self.create_maze(self.start_pos)

    def create_map(self) -> list:
        self.map = dict()
        self.not_marked = []
        self.stack = []
        # komplett mit Wänden befüllt:
        for row in range(self.row_max):
            for column in range(self.col_max):
                pos = (row, column)
                cur_cell = Cell(row, column)
                self.map[pos] = cur_cell
                self.not_marked += [cur_cell]
        
    def create_maze(self, pos):
        while len(self.not_marked) >= 1:
            cur_cell = self.map[pos]
            cur_cell.visited = True
            try:
                self.not_marked.remove(cur_cell)
            except ValueError:    # soll vorkommen
                pass

            neighbors = self.get_non_visited_neighbors(pos)
            if len(neighbors) < 1:
                #other_neighbor = self.get_pos_with_not_marked_neighbor()
                if len(self.stack) > 0:
                    pos = self.stack.pop(-1)
                else:
                    print("###########################UPPS###########################")
                    break
            else:
                if len(neighbors) > 1:
                    self.stack += [cur_cell.get_pos()]
                neighbor = random.choices(neighbors, k=1)
                cur_cell.remove(neighbor[0][1])
                self.map[neighbor[0][0]].remove_opposite(neighbor[0][1])
                pos = neighbor[0][0]

    def debug_create_maze(self):
        if len(self.not_marked) >= 1:
            cur_cell = self.map[self.pos]
            cur_cell.visited = True
            try:
                self.not_marked.remove(cur_cell)
            except ValueError:    # soll vorkommen
                pass

            neighbors = self.get_non_visited_neighbors(self.pos)
            if len(neighbors) < 1:
                #other_neighbor = self.get_pos_with_not_marked_neighbor()
                if len(self.stack) > 0:
                    self.pos = self.stack.pop(-1)
                else:
                    print("###########################UPPS###########################")
                    #break
            else:
                if len(neighbors) > 1:
                    self.stack += [cur_cell.get_pos()]
                neighbor = random.choices(neighbors, k=1)
                print(f"1. >>>>>>>>> P{cur_cell.get_pos()} -> entferne {neighbor[0][1]} Wand")
                cur_cell.remove(neighbor[0][1])
                print(f"2. >>>>>>>>> P{self.map[neighbor[0][0]].get_pos()} -> entferne gegenteil von {neighbor[0][1]} Wand")
                self.map[neighbor[0][0]].remove_opposite(neighbor[0][1])
                self.pos = neighbor[0][0]
                self.cur_pos = self.pos
        else:
            print("im finish")

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
                neighbors += [[(pos[0]-1, pos[1]), 'up']]
        if pos[0]+1 < self.row_max:
            if not self.map[(pos[0]+1, pos[1])].visited:
                neighbors += [[(pos[0]+1, pos[1]), 'down']]
        if pos[1]-1 >= self.col_min:
            if not self.map[(pos[0], pos[1]-1)].visited:
                neighbors += [[(pos[0], pos[1]-1), 'left']]
        if pos[1]+1 < self.col_max:
            if not self.map[(pos[0], pos[1]+1)].visited:
                neighbors += [[(pos[0], pos[1]+1), 'right']]
        return neighbors

    # get_pos_with_not_marked_neighbor -> durch stack ersetzt
    # -> es ist wichtig, dass nicht gleich die nachbarn sondern das schon gesuchte Zelle 
    # eingefügt wird!

    def draw_with_pygame(self, buffer=20, tile_size=50):
        import pygame
        pygame.init()
        screen = pygame.display.set_mode((self.col_max*tile_size+buffer*2, self.row_max*tile_size+buffer*2))
        pygame.display.set_caption("Maze Generation Test")
        clock = pygame.time.Clock()

        r = pygame.Rect(self.start_pos[1]*tile_size+tile_size//4+buffer, self.start_pos[0]*tile_size+tile_size//4+buffer, tile_size-tile_size//2, tile_size-tile_size//2)
        pygame.draw.rect(screen, (150, 250, 150), r)

        for row in range(self.row_max):
            for col in range(self.col_max):
                cur_cell = self.map[(row, col)]
                x = col*tile_size+buffer
                y = row*tile_size+buffer
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
                if cur_cell.right:
                    pygame.draw.line(screen, (255, 255, 255), [x+tile_size, y], [x+tile_size, y+tile_size])
        
        pygame.display.update()
        running = True
        while running:
            clock.tick(10)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

    def debug_draw_with_pygame(self):
        if not self.debug:
            raise ValueError('You have to be in debug mode!')
        import pygame
        running = True
        pygame.init()
        buffer = 20
        tile_size = 50
        screen = pygame.display.set_mode((self.col_max*tile_size+buffer*2 ,self.row_max*tile_size+buffer*2))
        pygame.display.set_caption("Maze Generation Test")
        clock = pygame.time.Clock()

        while running:

            r = pygame.Rect(0, 0, self.col_max*tile_size+buffer, self.row_max*tile_size+buffer)
            pygame.draw.rect(screen, (0, 0, 0), r)

            print("Cur-Pos:", self.cur_pos)
            r = pygame.Rect(self.cur_pos[1]*tile_size+tile_size//4+buffer, self.cur_pos[0]*tile_size+tile_size//4+buffer, tile_size-tile_size//2, tile_size-tile_size//2)
            pygame.draw.rect(screen, (150, 250, 150), r)

            for row in range(self.row_max):
                for col in range(self.col_max):
                    cur_cell = self.map[(row, col)]
                    x = col*tile_size+buffer
                    y = row*tile_size+buffer
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
                    if cur_cell.right:
                        pygame.draw.line(screen, (255, 255, 255), [x+tile_size, y], [x+tile_size, y+tile_size])
            
            pygame.display.update()
            running_mall_round = True
            while running_mall_round:
                clock.tick(10)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running_mall_round = False
                        running = False
                    if event.type == pygame.MOUSEBUTTONUP:
                        self.debug_create_maze()
                        running_mall_round = False

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
    maze.draw_with_pygame()
    #maze = Maze(debug=True)
    #maze.debug_draw_with_pygame()

    maze_2 = Maze(col_max=30, row_max=10)
    maze_2.draw_with_pygame()

    maze_3 = Maze(col_max=100, row_max=70)
    maze_3.draw_with_pygame(tile_size=10)
