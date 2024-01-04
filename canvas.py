import tkinter as tk
from brushes import PencilBrush, SprayBrush, EraserBrush


# Création de la classe Canvas, qui hérite de tk.Canvas
class Canvas(tk.Canvas):
    def __init__(self, master, **kwargs):
        super().__init__(master, bg="white", **kwargs)
        self.bind("<B1-Motion>", self.draw)
        self.color = "black"
        self.eraser_mode = False
        self.brush_size = 2
        self.current_brush = PencilBrush(self, size=self.brush_size)
        self.brush_size_label = None

    # Definit la fonction de dessin
    def draw(self, event):
        try:

            # Récupère les coordonnées de la souris
            x, y = event.x, event.y

            if self.eraser_mode:
                self.current_brush = EraserBrush(self, size=self.brush_size)
            elif isinstance(
                self.current_brush,
                PencilBrush
            ) and not self.eraser_mode:
                self.current_brush = PencilBrush(self, size=self.brush_size)
            elif isinstance(
                self.current_brush,
                SprayBrush
            ) and not self.eraser_mode:
                self.current_brush = SprayBrush(self, size=self.brush_size)

            self.current_brush.draw(x, y)

        except Exception as e:
            tk.messagebox.showerror(  # type: ignore
                "Error",
                f"An error occurred: {str(e)}"
            )

    def set_color(self, color):
        self.color = color

    def toggle_eraser_mode(self):
        self.eraser_mode = not self.eraser_mode

    def toggle_brush_mode(self):
        self.eraser_mode = False
        self.current_brush = PencilBrush(self, size=self.brush_size)

    def set_brush_size(self, size):
        self.brush_size = size
        self.update_brush_size_label()

    def toggle_spray_mode(self):
        self.eraser_mode = False
        self.current_brush = SprayBrush(self, size=self.brush_size)

    def set_brush_size_label(self, brush_size_label):
        self.brush_size_label = brush_size_label

    def update_brush_size_label(self):
        if self.brush_size_label:
            self.brush_size_label.config(
                text=f"Taille du pinceau: {self.brush_size}"
            )
