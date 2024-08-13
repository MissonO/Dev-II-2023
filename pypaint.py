import argparse
import tkinter as tk
from drawing_app import DrawingApp


def parse_args():
    """
    Parse the arguments
    POST: argparse.Namespace object with the parsed arguments
          with a background attribute with white as default value is returned
    """
    parser = argparse.ArgumentParser(
        description="Application de dessin")
    # bg or background argument, optional 
    # with an optional specification(nargs), default is white
    parser.add_argument('-bg', '--background', nargs='?', type=str,
                        default="white",
                        help="Couleur de fond")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    root = tk.Tk()
    app = DrawingApp(root, background=args.background)
    root.mainloop()
