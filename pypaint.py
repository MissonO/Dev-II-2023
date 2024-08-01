import argparse
import tkinter as tk
from drawing_app import DrawingApp


def parse_args():
    parser = argparse.ArgumentParser(
        description="Application de dessin avec Tkinter")
    parser.add_argument('--background', type=str,
                        default="white",
                        help="Couleur de fond du document")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    root = tk.Tk()
    app = DrawingApp(root, background=args.background)
    root.mainloop()
