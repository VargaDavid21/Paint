from tkinter import Frame, Button, TOP, LEFT


class Palette:
    def __init__(self, window, drawing_area):
        self.palette_frame = Frame(window)
        self.palette_frame.place(relx=0.0, rely=0.5, anchor='w')

        # Create frame for colors palette within palette_frame
        self.color_frame = Frame(self.palette_frame)
        self.color_frame.pack(side=TOP, padx=5, pady=5)

        colors = ["black", "red", "green", "blue", "yellow", "white"]
        for i, color_name in enumerate(colors):
            Button(self.color_frame, bg=color_name, width=2,
                   command=lambda color_name=color_name: drawing_area.change_color(color_name)).grid(row=i,
                                                                                                     column=0)  # Place buttons in the same column

        # Create frame for sizes palette within palette_frame
        self.size_frame = Frame(self.palette_frame)
        self.size_frame.pack(side=TOP, padx=5, pady=5)

        # Sizes palette
        sizes = [1, 2, 5, 10, 20]
        for i, size in enumerate(sizes):
            Button(self.size_frame, text=str(size), command=lambda size=size: drawing_area.change_width(size)).grid(
                row=i, column=0)  # Place buttons in the same column
