import tkinter as tk
from tkinter import colorchooser
from canvas import Canvas
from buttons import EraserButton, SizeButton, SprayButton


class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PyPaint")

        # Créationet affichage du canvas
        self.canvas = Canvas(
            root,
            width=800,
            height=600,
        )
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)

        brush_size_label = self.create_brush_size_label()
        self.canvas.set_brush_size_label(brush_size_label)

        # Bouton pour choisir la couleur
        color_button = tk.Button(
            root, text="Couleur",
            command=self.choose_color
        )
        color_button.pack(side=tk.RIGHT)

        eraser_button = EraserButton(root, self.canvas)
        eraser_button.pack(side=tk.LEFT)
        spray_button = SprayButton(root, self.canvas)
        spray_button.pack(side=tk.LEFT)
        size_button = SizeButton(root, self.canvas)
        size_button.pack(side=tk.LEFT)
        brush_size_label.pack(side=tk.LEFT)

    def choose_color(self):
        try:
            color = colorchooser.askcolor()[1]
            if color is not None:
                self.canvas.set_color(color)
        except Exception as e:
            tk.messagebox.showerror(  # type: ignore
                "Error",
                f"An error occurred: {str(e)}"
            )

    def create_brush_size_label(self):
        return tk.Label(
            self.root,
            text=f"Brush Size: {self.canvas.brush_size}"
        )
