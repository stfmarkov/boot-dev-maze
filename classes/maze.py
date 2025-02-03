from classes.cell import Cell
import time
import random

class Maze():
    BUFFER = 10

    def __init__(        
        self,
        num_rows,
        num_cols,
        win,
        seed = None
    ):
        
        if(seed != None):
            random.seed(seed)

        self.num_rows = num_rows
        self.num_cols = num_cols
        self.canvas = win.canvas

        self.cell_size_x = 0
        self.cell_size_y = 0

        self.win = win
        self._cells = []

        self.canvas.after(100, self._create_cells)

    def _create_cells(self):
        self.cell_size_x = (self.canvas.winfo_width() - 2*self.BUFFER) // self.num_cols
        self.cell_size_y = (self.canvas.winfo_height() - 2*self.BUFFER)// self.num_rows
        for col in range(self.num_cols):
            self._cells.append([])
            for row in range(self.num_rows):
                cell = Cell(self.win)
                self._cells[col].append(cell)

        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._draw_cells()        

    def _break_entrance_and_exit(self):
        self._cells[0][0].top_wall = False
        self._cells[self.num_cols - 1][self.num_rows - 1].bottom_wall = False


    def _draw_cells(self):
        for col in range(self.num_cols):
            for row in range(self.num_rows):
                x1 = col * self.cell_size_x + self.BUFFER
                x2 = x1 + self.cell_size_x 
                y1 = row * self.cell_size_y + self.BUFFER
                y2 = y1 + self.cell_size_y
                self._cells[col][row].draw(x1, x2, y1, y2)

    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)

    def _break_walls_r(self, row, col):
        self._cells[col][row].visited = True

        while True:
            possible_directions = []

            def add_direction(row, col, direction):
                if not self._cells[col][row].visited:
                    possible_directions.append({'row':row, 'col':col, 'direction':direction})

            is_left_most = col == 0
            is_right_most = col == self.num_cols - 1
            is_top_most = row == 0
            is_bottom_most = row == self.num_rows - 1

            if not is_left_most:
                add_direction(row, col - 1, 'left')    

            if not is_right_most:
                add_direction(row, col + 1, 'right')

            if not is_top_most:
                add_direction(row - 1, col, 'top')

            if not is_bottom_most:
                add_direction(row + 1, col, 'bottom')

            if len(possible_directions) == 0:
                return
            
            next = random.randrange(0, len(possible_directions))

            nextRow = possible_directions[next]['row']
            nextCol = possible_directions[next]['col']
            direction = possible_directions[next]['direction']

            if(direction == 'top'):
                self._cells[col][row].top_wall = False
                self._cells[nextCol][nextRow].bottom_wall = False

            if(direction == 'right'):
                self._cells[col][row].right_wall = False
                self._cells[nextCol][nextRow].left_wall = False

            if(direction == 'bottom'):
                self._cells[col][row].bottom_wall = False
                self._cells[nextCol][nextRow].top_wall = False

            if(direction == 'left'):
                self._cells[col][row].left_wall = False
                self._cells[nextCol][nextRow].right_wall = False

            self._break_walls_r(nextRow, nextCol)
