import argparse
import tkinter as tk
from drawing_app import DrawingApp


def parse_args():
    parser = argparse.ArgumentParser(
        description="Application de dessin")
    parser.add_argument('-bg', '--background', nargs='?', type=str,
                        default="white",
                        help="Couleur de fond")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    root = tk.Tk()
    app = DrawingApp(root, background=args.background)
    root.mainloop()
