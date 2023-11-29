import pytest
import tkinter as tk
from pypaint import DrawingApp, Canvas, EraserButton
from unittest.mock import patch


def test_canvas_initial_color():
    root = tk.Tk()
    canvas = Canvas(root)
    assert canvas.color == "black"


def test_canvas_set_color():
    root = tk.Tk()
    canvas = Canvas(root)
    canvas.set_color("red")
    assert canvas.color == "red"


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


def test_drawing_app_initialization(drawing_app):
    assert drawing_app.root.title() == "PyPaint"
    assert isinstance(drawing_app.canvas, Canvas)


def test_canvas_toggle_brush_mode(drawing_app):
    canvas = drawing_app.canvas

    canvas.toggle_eraser_mode()
    assert canvas.eraser_mode

    canvas.toggle_brush_mode()
    assert not canvas.eraser_mode


def test_eraser_button_toggle_eraser_mode(drawing_app):
    eraser_button = EraserButton(drawing_app.root, drawing_app.canvas)

    assert not drawing_app.canvas.eraser_mode
    assert eraser_button.cget("bg") == eraser_button.unselected_color

    eraser_button.toggle_eraser_mode()

    assert drawing_app.canvas.eraser_mode
    assert eraser_button.cget("bg") == eraser_button.selected_color


def test_choose_color_cancel(drawing_app):
    with patch('tkinter.colorchooser.askcolor', return_value=(None, None)):
        initial_color = drawing_app.canvas.color

        drawing_app.choose_color()

        assert drawing_app.canvas.color == initial_color


def test_choose_color_valid_color(drawing_app):
    with patch(
        'tkinter.colorchooser.askcolor',
        return_value=((255, 0, 0),
                      "#FF0000"
                      )
                ):

        drawing_app.choose_color()

        assert drawing_app.canvas.color == "#FF0000"


def test_canvas_set_brush_size():
    root = tk.Tk()
    canvas = Canvas(root)

    # Set the brush size to 10
    canvas.set_brush_size(10)
    assert canvas.brush_size == 10

    # Set the brush size to 5
    canvas.set_brush_size(5)
    assert canvas.brush_size == 5
