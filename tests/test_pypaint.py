import pytest
import tkinter as tk
from drawing_app import DrawingApp
from canvas import Canvas
from buttons import EraserButton, SprayButton, SizeButton
from unittest.mock import patch


# Tests for the Canvas initial color set as black
def test_canvas_initial_color():
    root = tk.Tk()
    canvas = Canvas(root)
    assert canvas.color == "black"


# Tests for the canvas color setting to red
def test_canvas_set_color():
    root = tk.Tk()
    canvas = Canvas(root)
    canvas.set_color("red")
    assert canvas.color == "red"


# Tests for the canvas drawing
def test_canvas_draw():
    root = tk.Tk()
    canvas = Canvas(root)

    # Simulate a mouse motion event
    event = tk.Event()
    event.x, event.y = 100, 100
    canvas.draw(event)

    # Assert that an oval with the correct color is created
    items = canvas.find_all()
    assert len(items) == 1
    assert canvas.itemcget(items[0], "fill") == canvas.color


@pytest.fixture
def mock_colorchooser():
    with patch('tkinter.colorchooser.askcolor') as mock:
        yield mock


@pytest.fixture
def drawing_app(request):
    root = tk.Tk()
    app = DrawingApp(root)
    yield app
    root.destroy()


# Tests for the DrawingApp initialization
def test_drawing_app_initialization(drawing_app):
    assert drawing_app.root.title() == "PyPaint"
    assert isinstance(drawing_app.canvas, Canvas)


# Tests for the DrawingApp brush mode enabling
def test_canvas_toggle_brush_mode(drawing_app):
    canvas = drawing_app.canvas

    canvas.toggle_eraser_mode()
    assert canvas.eraser_mode

    canvas.toggle_brush_mode()
    assert not canvas.eraser_mode


# Tests for the DrawingApp eraser mode enabling
def test_eraser_button_toggle_eraser_mode(drawing_app):
    eraser_button = EraserButton(drawing_app.root, drawing_app.canvas)

    assert not drawing_app.canvas.eraser_mode
    assert eraser_button.cget("bg") == eraser_button.unselected_color

    eraser_button.toggle_eraser_mode()

    assert drawing_app.canvas.eraser_mode
    assert eraser_button.cget("bg") == eraser_button.selected_color

    # Test when canvas.toggle_eraser_mode() raises an exception
    with patch.object(
        drawing_app.canvas,
        'toggle_eraser_mode',
        side_effect=Exception("Test Exception")
    ):
        with patch('tkinter.messagebox.showerror') as mock_showerror:
            eraser_button.toggle_eraser_mode()

    mock_showerror.assert_called_once_with(
        "Error", "An error occurred: Test Exception"
    )

    assert not drawing_app.canvas.eraser_mode
    assert eraser_button.cget("bg") == eraser_button.unselected_color


# Tests for the DrawingApp color choosing cancelation
def test_choose_color_cancel(drawing_app):
    with patch('tkinter.colorchooser.askcolor', return_value=(None, None)):
        initial_color = drawing_app.canvas.color

        drawing_app.choose_color()

        assert drawing_app.canvas.color == initial_color


# Tests for the DrawingApp color choosing
def test_choose_color_valid_color(drawing_app):
    with patch(
        'tkinter.colorchooser.askcolor',
        return_value=((255, 0, 0),
                      "#FF0000"
                      )
                ):

        drawing_app.choose_color()

        assert drawing_app.canvas.color == "#FF0000"


# Tests for the DrawingApp brush size setting
def test_canvas_set_brush_size():
    root = tk.Tk()
    canvas = Canvas(root)

    # Set the brush size to 10
    canvas.set_brush_size(10)
    assert canvas.brush_size == 10

    # Set the brush size to 5
    canvas.set_brush_size(5)
    assert canvas.brush_size == 5


def test_eraser_button_initialization():
    root = tk.Tk()
    canvas = Canvas(root)
    eraser_button = EraserButton(root, canvas)

    assert eraser_button.cget("text") == "Gomme"
    assert eraser_button.cget("bg") == eraser_button.unselected_color


def test_spray_button_initialization():
    root = tk.Tk()
    canvas = Canvas(root)
    spray_button = SprayButton(root, canvas)

    assert spray_button.cget("text") == "Toggle Brush"
    assert spray_button.cget("bg") == spray_button.unselected_color


def test_size_button_initialization():
    root = tk.Tk()
    canvas = Canvas(root)
    size_button = SizeButton(root, canvas)

    assert size_button.cget("text") == "Taille"
