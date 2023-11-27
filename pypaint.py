import tkinter as tk
from tkinter import colorchooser


# Création de la classe Canvas, qui hérite de tk.Canvas
class Canvas(tk.Canvas):
    def __init__(self, master, **kwargs):
        super().__init__(master, bg="white", **kwargs) # Appel du constructeur de tk.Canvas
        self.bind("<B1-Motion>", self.draw) # Lorsque le bouton gauche de la souris est maintenu enfoncé, on dessine
        self.color = "black"

    def draw(self, event): # Definit la fonction de dessin
        x, y = event.x, event.y # Récupère les coordonnées de la souris
        self.create_oval(x - 2, y - 2, x + 2, y + 2, fill="black") # Dessine un cercle de rayon 2 pixels
    
    def set_color(self, color):
        self.color = color
        self.update_idletasks()

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PyPaint")

        self.canvas = Canvas(root, width=800, height=600) # Création du canvas
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH) # Affichage du canvas

        # Bouton pour choisir la couleur
        color_button = tk.Button(root, text="Couleur", command=self.choose_color)
        color_button.pack(side=tk.LEFT)

    def choose_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.canvas.set_color(color)


if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()
