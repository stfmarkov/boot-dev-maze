from classes.point import Point
from classes.line import Line

class Cell():
    def __init__(self, win):
        self._win = win
        self.left_wall = True
        self.right_wall = True
        self.top_wall = True
        self.bottom_wall = True
        self.visited = False

    def draw(self, x1, x2, y1, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._center = Point((x1 + x2) // 2, (y1 + y2) // 2)

        if self.left_wall:
            self._win.drow_line(Line(Point(x1, y1), Point(x1, y2)))
        if self.right_wall:
            self._win.drow_line(Line(Point(x2, y1), Point(x2, y2)))
        if self.top_wall:
            self._win.drow_line(Line(Point(x1, y1), Point(x2, y1)))
        if self.bottom_wall:
            self._win.drow_line(Line(Point(x1, y2), Point(x2, y2)))

    def draw_move(self, to_cell, undo=False):
        color = "grey" if not undo else "red"
        self._win.drow_line(Line(self._center, to_cell._center), color)
                                
    def _solve_r(self, row, col, maze):
        # self._win._animate()
        self.visited = True
        is_end_cell = row == maze.num_rows - 1 and col == maze.num_cols - 1

        if is_end_cell:
            return True
        
        possible_directions = []

        def add_direction(row, col, direction):
            has_wall = (direction == 'left' and self.left_wall) or (direction == 'right' and self.right_wall) or (direction == 'top' and self.top_wall) or (direction == 'bottom' and self.bottom_wall)
            if not maze._cells[col][row].visited and not has_wall:
                possible_directions.append({'row':row, 'col':col, 'direction':direction})

        is_left_most = col == 0
        is_right_most = col == maze.num_cols - 1
        is_top_most = row == 0
        is_bottom_most = row == maze.num_rows - 1

        if not is_left_most:
            add_direction(row, col - 1, 'left')    

        if not is_right_most:
            add_direction(row, col + 1, 'right')

        if not is_top_most:
            add_direction(row - 1, col, 'top')

        if not is_bottom_most:
            add_direction(row + 1, col, 'bottom')

        for direction in possible_directions:
            cell = maze._cells[direction['col']][direction['row']]
            if cell._solve_r(direction['row'], direction['col'], maze):
                self.draw_move(cell)
                return True
            cell.draw_move(self, undo=True)
            

        return False