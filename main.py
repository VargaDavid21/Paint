from tkinter import Tk
from paint_app import PaintApp


def close(event):
    root.destroy()


if __name__ == "__main__":
    root = Tk()
    root.bind('<Escape>', close)  # Bind the Escape key to the close function
    PaintApp(root)
    root.mainloop()
