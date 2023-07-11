from tkinter import Canvas, BOTH


class DrawingArea:
    def __init__(self, window):
        self.drawing_area = Canvas(window, bg="white")
        self.drawing_area.pack(fill=BOTH, expand=True)
        self.last_x, self.last_y = 0, 0
        self.color = "black"
        self.width = 5  # Default line width
        self.drawing_area.bind("<Button-1>", self.start_line)
        self.drawing_area.bind("<ButtonRelease-1>", self.end_line)
        window.bind_all('<Control-r>', self.clear_canvas)  # Bind Ctrl+R to clear_canvas function

    def draw(self, event):
        x, y = event.x, event.y
        self.drawing_area.create_line((self.last_x, self.last_y, x, y), fill=self.color, width=self.width)
        self.last_x, self.last_y = x, y

    def start_line(self, event):
        self.last_x, self.last_y = event.x, event.y
        self.drawing_area.bind("<B1-Motion>", self.draw)

    def end_line(self, event):
        self.drawing_area.unbind("<B1-Motion>")

    def clear_canvas(self, event):  # Event handler for Ctrl+R
        self.drawing_area.delete("all")  # Clear the canvas

    def change_color(self, new_color):
        self.color = new_color

    def change_width(self, new_width):  # Function to change width of line
        self.width = new_width
