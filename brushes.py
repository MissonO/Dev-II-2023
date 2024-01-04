import random


# Classe de pinceau de base
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


# Classe pour le crayon héritant de la classe Brush
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


# Classe pour le spray héritant de la classe Brush
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


# Classe pour la gomme héritant de la classe Brush
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
