import tkinter as tk
from brushes import PencilBrush, SprayBrush, EraserBrush


# Création de la classe Canvas, qui hérite de tk.Canvas
class Canvas(tk.Canvas):
    def __init__(self, master, **kwargs):
        """
        Create a canvas
        PRE: master is a tkinter widget and kwargs are the arguments for the
             canvas
        POST: a canvas is created associated with the master widget
              with the draw method bound to the left click,
              the default color is set to black,
              the eraser mode is set to False
              and the brush size is set to 2"""
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
        """
        Draw on the canvas
        PRE: event is a tkinter event with x and y coordinates
             self is an instance of Canvas with eraser_mode,
             brush_size and current_brush
        POST: the brush draws on the canvas on the selected x and y coordinates
              self.current_brush is updated
        RAISE: tk.messagebox.showerror if an error occurs
        """
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
        """
        Set the color of the brush
        PRE: color is a string and a color
        POST: self.color is updated
        """
        self.color = color

    # Definit la fonction de changement de mode gomme
    def toggle_eraser_mode(self):
        """
        Toggle the eraser mode
        PRE: self is an instance of Canvas with a boolean eraser_mode
        POST: the eraser mode is toggled
        """
        self.eraser_mode = not self.eraser_mode

    # Definit la fonction de changement de mode crayon
    def toggle_brush_mode(self):
        """
        Toggle the brush mode
        PRE: self is an instance of Canvas with a boolean eraser_mode
             and current_brush
        POST: the eraser_mode is set to false and the brush mode is toggled
             with the pencil size
        """
        self.eraser_mode = False
        self.current_brush = PencilBrush(self, size=self.brush_size)

    # Definit la fonction de changement de taille du pinceau
    def set_brush_size(self, size):
        """
        Set the brush size
        PRE: size is an integer and self is an instance of Canvas
             with brush_size attribute
        POST: self.brush_size is updated and update_brush_size_label is called
        """
        self.brush_size = size
        self.update_brush_size_label()

    # Definit la fonction de changement de mode spray
    def toggle_spray_mode(self):
        """
        Toggle the spray mode
        PRE: self is an instance of Canvas with a boolean eraser_mode
             and current_brush
        POST: the eraser_mode is set to false and the brush mode is toggled
            with the spray size
        """
        self.eraser_mode = False
        self.current_brush = SprayBrush(self, size=self.brush_size)

    # Definit la fonction d'initialisation de label de taille du pinceau
    def set_brush_size_label(self, brush_size_label):
        """
        Set the brush size label
        PRE: brush_size_label is a tkinter label, self is an instance of Canvas
        POST: self.brush_size_label is updated
        """
        self.brush_size_label = brush_size_label

    # Definit la fonction de mise à jour du label de taille du pinceau
    def update_brush_size_label(self):
        """
        Update the brush size label
        PRE: self is an instance of Canvas with brush_size_label
        POST: the brush size label is updated
        """
        if self.brush_size_label:
            self.brush_size_label.config(
                text=f"Taille du pinceau: {self.brush_size}"
            )
