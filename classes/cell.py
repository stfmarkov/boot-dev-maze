from classes.point import Point
from classes.line import Line

class Cell():
    def __init__(self, win):
        self._win = win
        self.left_wall = True
        self.right_wall = True
        self.top_wall = True
        self.bottom_wall = True

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
                                