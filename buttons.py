import tkinter as tk
from PIL import Image
from tkinter import messagebox, simpledialog, filedialog, colorchooser
from brushes import PencilBrush, SprayBrush


# Classe bouton générique héritant de tk.Button
class Button(tk.Button):
    def __init__(self, master, canvas, text, command, **kwargs):
        super().__init__(
            master,
            text=text,
            command=command,
            **kwargs
        )
        self.canvas = canvas
        self.selected_color = "lightgrey"
        self.unselected_color = "SystemButtonFace"
        self.configure(bg=self.unselected_color)

    def reset_other_buttons(self):
        for button in self.all_buttons:  # type: ignore
            if button is not self:
                button.configure(bg=button.unselected_color)


# Classe bouton pour la gomme héritant de la classe Button
class EraserButton(Button):
    def __init__(self, master, canvas, **kwargs):
        super().__init__(
            master,
            canvas,
            "Gomme",
            self.toggle_eraser_mode,
            **kwargs
        )

    def toggle_eraser_mode(self):
        try:
            self.canvas.toggle_eraser_mode()
            self.reset_other_buttons()
            if self.canvas.eraser_mode:
                self.configure(bg=self.selected_color)
            else:
                self.canvas.toggle_brush_mode()
                self.configure(bg=self.unselected_color)
        except Exception as e:
            tk.messagebox.showerror(  # type: ignore
                "Error",
                f"An error occurred: {str(e)}"
            )
            self.canvas.eraser_mode = False
            self.configure(bg=self.unselected_color)


# Classe bouton pour la taille du pinceau héritant de la classe Button
class SizeButton(Button):
    def __init__(self, master, canvas, **kwargs):
        super().__init__(
            master,
            canvas,
            "Taille",
            self.choose_size,
            **kwargs
        )

    def choose_size(self):
        try:
            size = simpledialog.askinteger(
                "Brush Size",
                "Enter brush size:",
                initialvalue=self.canvas.brush_size
            )
            if size is not None:
                self.canvas.brush_size = size
                self.canvas.update_brush_size_label()
        except Exception as e:
            messagebox.showerror(
                "Error",
                f"An error occurred: {str(e)}"
            )


# Classe bouton pour le spray héritant de la classe Button
class SprayButton(Button):
    def __init__(self, master, canvas, **kwargs):
        super().__init__(
            master,
            canvas,
            "Toggle Brush",
            self.toggle_brush_type,
            **kwargs
        )
        self.brush_types = [PencilBrush, SprayBrush]
        self.current_brush_index = 0

    def toggle_brush_type(self):
        try:
            self.reset_other_buttons()
            self.current_brush_index = (
                self.current_brush_index + 1
            ) % len(self.brush_types)
            brush_type = self.brush_types[self.current_brush_index]

            if brush_type == PencilBrush:
                self.canvas.toggle_brush_mode()
                self.configure(bg=self.unselected_color)
            elif brush_type == SprayBrush:
                self.canvas.toggle_spray_mode()
                self.configure(bg=self.selected_color)
        except Exception as e:
            tk.messagebox.showerror(  # type: ignore
                "Error",
                f"An error occurred: {str(e)}"
            )


class SaveButton(Button):
    def __init__(self, master, canvas, **kwargs):
        super().__init__(
            master,
            canvas,
            "Sauvegarder",
            self.save_image,
            **kwargs
        )

    def save_image(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".jpg",
            filetypes=[
                ("JPEG", "*.jpg"),
                ("PNG", "*.png"),
                ("GIF", "*.gif"),
            ]
        )
        if not file_path:
            return

        self.canvas.postscript(file="temp.ps", colormode='color')

        image = Image.open("temp.ps")
        image.save(file_path, "JPEG")


class colorButton(Button):
    def __init__(self, master, canvas, **kwargs):
        super().__init__(
            master,
            canvas,
            "Couleur",
            self.choose_color,
            **kwargs
        )

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
