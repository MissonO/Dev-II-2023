import tkinter as tk
from PIL import Image
from tkinter import messagebox, simpledialog, filedialog, colorchooser
from brushes import PencilBrush, SprayBrush


# Classe bouton générique héritant de tk.Button
class Button(tk.Button):
    def __init__(self, master, canvas, text, command, **kwargs):
        """
        Create a generic button
        PRE: master is a tkinter widget, canvas is a Canvas object,
             text is a string, command is a function to execute
        POST: a button is created with the given text and command
              and the default color is set to unselected_color
        """
        super().__init__(
            master,
            text=text,
            command=command,
            **kwargs
        )
        self.canvas = canvas
        self.selected_color = "lightgrey"  # Couleur sélectionnée
        self.unselected_color = "SystemButtonFace"  # Couleur non sélectionnée
        self.configure(bg=self.unselected_color)

    # Reset les autres boutons sur la couleur non sélectionnée
    def reset_other_buttons(self):
        """
        Reset all buttons to unselected color except self

        PRE: self is a list of buttons
        POST: all buttons are reset to unselected color except self
        """
        for button in self.all_buttons:  # type: ignore
            if button is not self:
                button.configure(bg=button.unselected_color)


# Classe bouton pour la gomme héritant de la classe Button
class EraserButton(Button):
    def __init__(self, master, canvas, **kwargs):
        """
        Create an eraser button
        PRE: master is a tkinter widget, canvas is a Canvas object
        POST: an eraser button is created with the default text "Gomme"
             and the toggle_eraser_mode command attributed
        """
        super().__init__(
            master,
            canvas,
            text="Gomme",
            command=self.toggle_eraser_mode,
            **kwargs
        )

    # Active la gomme
    def toggle_eraser_mode(self):
        """
        Toggle eraser mode on and off

        PRE: self.canvas is a button with a configure method
        POST: eraser mode is toggled on and off
        RAISE: tk.messagebox.showerror if an error occurs
        """
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
        """
        Create a size button
        PRE: master is a tkinter widget, canvas is a Canvas object
        POST: a size button is created with the default text "Taille"
            and the choose_size command attributed
        """
        super().__init__(
            master,
            canvas,
            text="Taille",
            command=self.choose_size,
            **kwargs
        )

    # Choix de la taille du pinceau
    def choose_size(self):
        """
        Choose the brush size
        PRE: self is a button with canvas
        POST: the brush size is chosen
        RAISE: tk.messagebox.showerror if an error occurs
        """
        try:
            size = simpledialog.askinteger(
                "Taille du pinceau",
                "Choisissez la taille du pinceau:",
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
        """
        Create a spray button
        PRE: master is a tkinter widget, canvas is a Canvas object
        POST: a spray button is created with the default text "Spray"
            and the toggle_brush_type command attributed
        """
        super().__init__(
            master,
            canvas,
            text="Spray",
            command=self.toggle_brush_type,
            **kwargs
        )
        self.brush_types = [PencilBrush, SprayBrush]
        self.current_brush_index = 0

    # Active le spray
    def toggle_brush_type(self):
        """
        Toggle between brush types
        PRE: self is a button with brush_types and current_brush_index
        POST: the choosen brush type is toggled
        RAISE: tk.messagebox.showerror if an error occurs
        """
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


# Classe bouton pour la sauvegarde héritant de la classe Button
class SaveButton(Button):
    """
    Create a save button
    PRE: master is a tkinter widget, canvas is a Canvas object
    POST: a save button is created with the default text "Sauvegarder"
        and the save_image command attributed
    """
    def __init__(self, master, canvas, **kwargs):
        super().__init__(
            master,
            canvas,
            text="Sauvegarder",
            command=self.save_image,
            **kwargs
        )

    # Sauvegarde l'image
    def save_image(self):
        """
        Save the image
        PRE: self is a button with canvas
        POST: the image is saved in the chosen format
        """
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


# Classe bouton pour la couleur héritant de la classe Button
class ColorButton(Button):
    def __init__(self, master, canvas, **kwargs):
        """
        Create a color button
        PRE: master is a tkinter widget, canvas is a Canvas object
        POST: a color button is created with the default text "Couleur"
            and the choose_color command attributed
        """
        super().__init__(
            master,
            canvas,
            text="Couleur",
            command=self.choose_color,
            **kwargs
        )

    # Choix de la couleur
    def choose_color(self):
        """
        Choose the color
        PRE: self is a button with canvas
        POST: the color is chosen
        RAISE: tk.messagebox.showerror if an error occurs
        """
        try:
            color = colorchooser.askcolor()[1]
            if color is not None:
                self.canvas.set_color(color)
        except Exception as e:
            tk.messagebox.showerror(  # type: ignore
                "Error",
                f"An error occurred: {str(e)}"
            )
