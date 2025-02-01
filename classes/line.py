from tkinter import Canvas

class Line():
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def draw(self, canvas: Canvas, color="black"):

        canvas.create_line(
            self.start.x, 
            self.start.y, 
            self.end.x, 
            self.end.y, 
            fill=color, 
            width=2
        )

    def __repr__(self):
        return f"Line({self.start}, {self.end})"