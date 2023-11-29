import pytest
import tkinter as tk
from pypaint import DrawingApp, Canvas, BrushButton, EraserButton
from unittest.mock import patch
from pyvirtualdisplay import Display


@pytest.fixture(scope="session")
def virtual_display():
    with Display(visible=0, size=(800, 600), backend="xvfb") as disp:
        yield disp


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
def drawing_app(request, virtual_display):
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


def test_brush_button_toggle_brush_mode(drawing_app):
    brush_button = BrushButton(drawing_app.root, drawing_app.canvas)

    assert not drawing_app.canvas.eraser_mode
    assert brush_button.cget("bg") == brush_button.unselected_color

    brush_button.toggle_brush_mode()

    assert not drawing_app.canvas.eraser_mode
    assert brush_button.cget("bg") == brush_button.selected_color


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
