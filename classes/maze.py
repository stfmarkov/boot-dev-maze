from classes.cell import Cell
import time

class Maze():
    BUFFER = 10

    def __init__(        
        self,
        num_rows,
        num_cols,
        win,
    ):
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

        self._draw_cells()

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
