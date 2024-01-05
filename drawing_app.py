import tkinter as tk
from canvas import Canvas
from buttons import EraserButton, SprayButton, SizeButton, SaveButton
from buttons import ColorButton


class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PyPaint")

        # Création et affichage du canvas
        self.canvas = Canvas(
            root,
            width=800,
            height=600,
        )
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)

        brush_size_label = self.create_brush_size_label()
        self.canvas.set_brush_size_label(brush_size_label)

        self.buttons = []

        # Bouton gomme
        eraser_button = EraserButton(root, self.canvas)
        eraser_button.pack(side=tk.LEFT)
        self.buttons.append(eraser_button)

        # Bouton spray
        spray_button = SprayButton(root, self.canvas)
        spray_button.pack(side=tk.LEFT)
        self.buttons.append(spray_button)

        # Bouton taille du pinceau
        size_button = SizeButton(root, self.canvas)
        size_button.pack(side=tk.LEFT)
        self.buttons.append(size_button)

        # Label de taille du pinceau
        brush_size_label.pack(side=tk.LEFT)

        # Bouton couleur
        color_button = ColorButton(root, self.canvas)
        color_button.pack(side=tk.LEFT)
        self.buttons.append(color_button)

        # Bouton sauvegarde
        save_button = SaveButton(root, self.canvas)
        save_button.pack(side=tk.RIGHT)
        self.buttons.append(save_button)

        for button in self.buttons:
            button.all_buttons = self.buttons

    # Création du label de taille du pinceau
    def create_brush_size_label(self):
        return tk.Label(
            self.root,
            text=f"Taille du pinceau: {self.canvas.brush_size}"
        )
