import pytest
import tkinter as tk
from pypaint import Canvas, DrawingApp
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


def test_choose_color_with_color_selection(drawing_app, mock_colorchooser):
    mock_colorchooser.return_value = (None, "#FF0000")

    drawing_app.choose_color()

    assert drawing_app.canvas.color == "#FF0000"
    assert drawing_app.canvas.set_color.call_count == 1
    drawing_app.canvas.set_color.assert_called_with("#FF0000")


def test_choose_color_with_cancel(drawing_app, mock_colorchooser):
    mock_colorchooser.return_value = (None, None)  # Simulate cancel
    initial_color = drawing_app.canvas.color

    drawing_app.choose_color()

    assert drawing_app.canvas.color == initial_color
    assert drawing_app.canvas.set_color.call_count == 0
