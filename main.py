from classes.window import Window
from classes.point import Point
from classes.line import Line

def main():
    win = Window(800, 600)

    line_1 = Line(Point(100, 100), Point(200, 200))
    line_2 = Line(Point(150, 150), Point(250, 250))

    win.drow_line(line_1, "red")
    win.drow_line(line_2, "blue")

    win.run()

    win.wait_for_close()

main()