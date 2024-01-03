import tkinter as tk
from brushes import PencilBrush, SprayBrush


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
        try:
            self.canvas.toggle_eraser_mode()
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
        try:
            size = tk.simpledialog.askinteger(  # type: ignore
                "Brush Size",
                "Enter brush size:",
                initialvalue=self.canvas.brush_size
            )
            if size is not None:
                self.canvas.brush_size = size
                self.canvas.update_brush_size_label()
        except Exception as e:
            tk.messagebox.showerror(  # type: ignore
                "Error",
                f"An error occurred: {str(e)}"
            )


class SprayButton(tk.Button):
    def __init__(self, master, canvas, **kwargs):
        super().__init__(
            master,
            text="Toggle Brush",
            command=self.toggle_brush_type,
            **kwargs
        )
        self.canvas = canvas
        self.brush_types = [PencilBrush, SprayBrush]
        self.current_brush_index = 0
        self.selected_color = "lightgrey"
        self.unselected_color = "SystemButtonFace"
        self.configure(bg=self.unselected_color)

    def toggle_brush_type(self):
        try:
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
