from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Maze")
        self.canvas = Canvas(self.root, width=width, height=height)
        self.canvas.pack(fill=BOTH, expand=True)
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.canvas.delete("all")
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        if self.running:
            self.redraw()
            self.root.after(100, self.wait_for_close)

    def close(self):
        self.running = False
        self.root.destroy()

    def drow_line(self, line, color="black"):
        line.draw(self.canvas, color)

    def run(self):
        self.running = True
        self.root.mainloop()

