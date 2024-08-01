import tkinter as tk
from brushes import PencilBrush, SprayBrush, EraserBrush


# Création de la classe Canvas, qui hérite de tk.Canvas
class Canvas(tk.Canvas):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)  # Création du canvas
        self.bind("<B1-Motion>", self.draw)  # Dessine lors du clic gauche
        self.color = "black"  # Couleur du pinceau
        self.eraser_mode = False  # Mode gomme
        self.brush_size = 2  # Taille du pinceau
        # Pinceau actuel
        self.current_brush = PencilBrush(self, size=self.brush_size)
        self.brush_size_label = None  # Label de taille du pinceau

    # Definit la fonction de dessin
    def draw(self, event):
        try:

            # Récupère les coordonnées de la souris
            x, y = event.x, event.y

            # Si le mode gomme est activé, on utilise le pinceau gomme
            if self.eraser_mode:
                self.current_brush = EraserBrush(self, size=self.brush_size)
            # Sinon, on utilise le crayon
            elif isinstance(
                self.current_brush,
                PencilBrush
            ) and not self.eraser_mode:
                self.current_brush = PencilBrush(self, size=self.brush_size)
            # Sinon, on utilise le  spray
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

    # Definit la fonction de changement de couleur
    def set_color(self, color):
        self.color = color

    # Definit la fonction de changement de mode gomme
    def toggle_eraser_mode(self):
        self.eraser_mode = not self.eraser_mode

    # Definit la fonction de changement de mode crayon
    def toggle_brush_mode(self):
        self.eraser_mode = False
        self.current_brush = PencilBrush(self, size=self.brush_size)

    # Definit la fonction de changement de taille du pinceau
    def set_brush_size(self, size):
        self.brush_size = size
        self.update_brush_size_label()

    # Definit la fonction de changement de mode spray
    def toggle_spray_mode(self):
        self.eraser_mode = False
        self.current_brush = SprayBrush(self, size=self.brush_size)

    # Definit la fonction d'initialisation de label de taille du pinceau
    def set_brush_size_label(self, brush_size_label):
        self.brush_size_label = brush_size_label

    # Definit la fonction de mise à jour du label de taille du pinceau
    def update_brush_size_label(self):
        if self.brush_size_label:
            self.brush_size_label.config(
                text=f"Taille du pinceau: {self.brush_size}"
            )
