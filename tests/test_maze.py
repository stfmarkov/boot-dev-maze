import unittest
from classes.maze import Maze
from classes.window import Window

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        win = Window(800, 600)
        m1 = Maze(num_rows, num_cols, win)

        def check_cols_rows():
            print(m1._cells)

            self.assertEqual(
                len(m1._cells),
                num_cols,
            )
            self.assertEqual(
                len(m1._cells[0]),
                num_rows,
            )

        win.canvas.after(100, check_cols_rows)
