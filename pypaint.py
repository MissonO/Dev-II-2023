import tkinter as tk
from tkinter import colorchooser


class Brush:
    def __init__(self, canvas, color="black"):
        self.canvas = canvas
        self.color = color

    def draw(self, x, y):
        raise NotImplementedError()

    def set_color(self, color):
        self.color = color


class PencilBrush(Brush):
    def draw(self, x, y):
        self.set_color(self.canvas.color)
        self.canvas.create_oval(
            x - 2,
            y - 2,
            x + 2,
            y + 2,
            fill=self.color,
            outline=self.color
        )


class EraserBrush(Brush):
    def draw(self, x, y):
        self.canvas.create_rectangle(
            x - 5,
            y - 5,
            x + 5,
            y + 5,
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

    # Definit la fonction de dessin
    def draw(self, event):

        # Récupère les coordonnées de la souris
        x, y = event.x, event.y

        if self.eraser_mode:
            self.brush = EraserBrush(self)
        else:
            self.brush = PencilBrush(self)

        self.brush.draw(x, y)

    def set_color(self, color):
        self.color = color

    def toggle_eraser_mode(self):
        self.eraser_mode = not self.eraser_mode

    def toggle_brush_mode(self):
        self.eraser_mode = False


class BrushButton(tk.Button):
    def __init__(self, master, canvas, **kwargs):
        super().__init__(
            master,
            text="Pinceau",
            command=self.toggle_brush_mode,
            **kwargs
        )
        self.canvas = canvas
        self.selected_color = "lightgrey"
        self.unselected_color = "SystemButtonFace"
        self.configure(bg=self.unselected_color)

    def toggle_brush_mode(self):
        self.canvas.toggle_brush_mode()
        if self.canvas.eraser_mode:
            self.configure(bg=self.unselected_color)
        else:
            self.configure(bg=self.selected_color)


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

        brush_button = BrushButton(root, self.canvas)
        brush_button.pack(side=tk.LEFT)
        eraser_button = EraserButton(root, self.canvas)
        eraser_button.pack(side=tk.LEFT)

    def choose_color(self):
        color = colorchooser.askcolor()[1]
        if color is not None:
            self.canvas.set_color(color)


if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()
