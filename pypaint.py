import tkinter as tk
from tkinter import colorchooser, simpledialog
import random


class Brush:
    def __init__(self, canvas, color="black", size=2):
        self.canvas = canvas
        self.color = color
        self.size = size

    def draw(self, x, y):
        raise NotImplementedError()

    def set_color(self, color):
        self.color = color

    def set_size(self, size):
        self.size = size


class PencilBrush(Brush):
    def draw(self, x, y):
        self.set_color(self.canvas.color)
        self.canvas.create_oval(
            x - self.size,
            y - self.size,
            x + self.size,
            y + self.size,
            fill=self.color,
            outline=self.color
        )


class SprayBrush(Brush):
    def draw(self, x, y):
        density = 5
        for _ in range(density):
            spray_x = x + random.uniform(-self.size, self.size)
            spray_y = y + random.uniform(-self.size, self.size)
            self.set_color(self.canvas.color)
            self.canvas.create_oval(
                spray_x - 1,
                spray_y - 1,
                spray_x + 1,
                spray_y + 1,
                fill=self.color,
                outline=self.color
            )


class EraserBrush(Brush):
    def draw(self, x, y):
        self.canvas.create_oval(
            x - self.size,
            y - self.size,
            x + self.size,
            y + self.size,
            fill="white",
            outline="white"
        )


# Création de la classe Canvas, qui hérite de tk.Canvas
class Canvas(tk.Canvas):
    def __init__(self, master, **kwargs):
        super().__init__(master, bg="white", **kwargs)
        self.bind("<B1-Motion>", self.draw)
        self.color = "black"
        self.eraser_mode = False
        self.brush_size = 2
        self.current_brush = PencilBrush(self, size=self.brush_size)

    # Definit la fonction de dessin
    def draw(self, event):

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

    def set_color(self, color):
        self.color = color

    def toggle_eraser_mode(self):
        self.eraser_mode = not self.eraser_mode

    def toggle_brush_mode(self):
        self.eraser_mode = False
        self.current_brush = PencilBrush(self, size=self.brush_size)

    def set_brush_size(self, size):
        self.brush_size = size

    def toggle_spray_mode(self):
        self.eraser_mode = False
        self.current_brush = SprayBrush(self, size=self.brush_size)

    def update_brush_size_label(self):
        brush_size_label.config(text=f"Brush Size: {self.brush_size}")


class EraserButton(tk.Button):
    def __init__(self, master, canvas, **kwargs):
        super().__init__(
            master,
            text="Gomme",
            command=self.toggle_eraser_mode,
            **kwargs
        )
        self.canvas = canvas
        self.selected_color = "lightgrey"
        self.unselected_color = "SystemButtonFace"
        self.configure(bg=self.unselected_color)

    def toggle_eraser_mode(self):
        self.canvas.toggle_eraser_mode()
        if self.canvas.eraser_mode:
            self.configure(bg=self.selected_color)
        else:
            self.configure(bg=self.unselected_color)


class SizeButton(tk.Button):
    def __init__(self, master, canvas, **kwargs):
        super().__init__(
            master,
            text="Taille",
            command=self.choose_size,
            **kwargs
        )
        self.canvas = canvas

    def choose_size(self):
        size = tk.simpledialog.askinteger(
            "Brush Size",
            "Enter brush size:",
            initialvalue=self.canvas.brush_size
        )
        if size is not None:
            self.canvas.brush_size = size
            self.canvas.update_brush_size_label()


class SprayButton(tk.Button):
    def __init__(self, master, canvas, **kwargs):
        super().__init__(
            master,
            text="Spray",
            command=self.toggle_spray_mode,
            **kwargs
        )
        self.canvas = canvas

    def toggle_spray_mode(self):
        self.canvas.toggle_spray_mode()


class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PyPaint")

        # Créationet affichage du canvas
        self.canvas = Canvas(root, width=800, height=600)
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)

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
        global brush_size_label
        brush_size_label = tk.Label(
            root,
            text=f"Brush Size: {self.canvas.brush_size}"
        )
        brush_size_label.pack(side=tk.LEFT)

    def choose_color(self):
        color = colorchooser.askcolor()[1]
        if color is not None:
            self.canvas.set_color(color)


if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()
