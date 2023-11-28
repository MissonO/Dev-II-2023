import tkinter as tk
from tkinter import colorchooser


# Création de la classe Canvas, qui hérite de tk.Canvas
class Canvas(tk.Canvas):
    def __init__(self, master, **kwargs):

        # Appel du constructeur de tk.Canvas
        super().__init__(master, bg="white", **kwargs)

        # Dessine lorsque le bouton gauche est enfonce
        self.bind("<B1-Motion>", self.draw)
        self.color = "black"

    # Definit la fonction de dessin
    def draw(self, event):

        # Récupère les coordonnées de la souris
        x, y = event.x, event.y

        # Dessine un cercle de rayon 2 pixels
        self.create_oval(
            x - 2,
            y - 2,
            x + 2,
            y + 2,
            fill=self.color,
            outline=self.color
        )

    def set_color(self, color):
        self.color = color


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
        color_button.pack(side=tk.LEFT)

    def choose_color(self):
        color = colorchooser.askcolor()[1]
        if color is not None:
            self.canvas.set_color(color)


if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()