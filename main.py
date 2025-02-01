from classes.window import Window
from classes.point import Point
from classes.line import Line
from classes.cell import Cell
from classes.maze import Maze

def main():
    win = Window(800, 600)

    # cell1 = Cell(win)
    # cell2 = Cell(win)
    # cell3 = Cell(win)
    # cell4 = Cell(win)

    # cell1.left_wall = False
    # cell1.right_wall = False

    # cell2.left_wall = False
    # cell2.bottom_wall = False

    # cell3.right_wall = False

    # cell4.left_wall = False
    # cell4.top_wall = False

    # cell1.draw(100, 200, 100, 200)
    # cell2.draw(200, 300, 100, 200)
    # cell3.draw(100, 200, 200, 300)
    # cell4.draw(200, 300, 200, 300)

    # cell1.draw_move(cell2)
    # cell2.draw_move(cell4)
    # cell4.draw_move(cell3)

    maze = Maze(10, 10, win)

    win.run()

    win.wait_for_close()

main()