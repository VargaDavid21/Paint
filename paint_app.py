from drawing_area import DrawingArea
from palette import Palette


class PaintApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Python Paint App")
        self.window.attributes('-fullscreen', True)  # Add this line

        # Create instances of DrawingArea and Palette
        self.drawing_area = DrawingArea(window)
        self.palette = Palette(window, self.drawing_area)
