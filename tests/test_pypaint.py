import pytest
import tkinter as tk
from drawing_app import DrawingApp
from canvas import Canvas
from buttons import EraserButton, SprayButton, SizeButton
from buttons import ColorButton, SaveButton
from unittest.mock import patch, Mock, MagicMock


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


# Test for the buttons
@pytest.fixture
def mock_canvas():
    return Mock()


@pytest.fixture
def mock_master():
    return MagicMock()


def test_eraser_button(mock_master, mock_canvas):
    eraser_button = EraserButton(mock_master, mock_canvas)
    eraser_button.cget = MagicMock(return_value="Gomme")
    assert eraser_button.cget("text") == "Gomme"


def test_size_button(mock_master, mock_canvas):
    size_button = SizeButton(mock_master, mock_canvas)
    size_button.cget = MagicMock(return_value="Taille")
    assert size_button.cget("text") == "Taille"


def test_spray_button(mock_master, mock_canvas):
    spray_button = SprayButton(mock_master, mock_canvas)
    spray_button.cget = MagicMock(return_value="Toggle Brush")
    assert spray_button.cget("text") == "Toggle Brush"


def test_save_button(mock_master, mock_canvas):
    save_button = SaveButton(mock_master, mock_canvas)
    save_button.cget = MagicMock(return_value="Sauvegarder")
    assert save_button.cget("text") == "Sauvegarder"


def test_color_button(mock_master, mock_canvas):
    color_button = ColorButton(mock_master, mock_canvas)
    color_button.cget = MagicMock(return_value="Couleur")
    assert color_button.cget("text") == "Couleur"


def test_size_button_choose_size(mock_master, mock_canvas):
    size_button = SizeButton(mock_master, mock_canvas)
    mock_canvas.update_brush_size_label = MagicMock()
    with patch('tkinter.simpledialog.askinteger', return_value=10):
        size_button.choose_size()
    assert mock_canvas.brush_size == 10
    mock_canvas.update_brush_size_label.assert_called_once()


def test_save_button_save_image(mock_master, mock_canvas):
    save_button = SaveButton(mock_master, mock_canvas)
    with patch(
            'tkinter.filedialog.asksaveasfilename',
            return_value='test.jpg'
         ), \
            patch('PIL.Image.open'), \
            patch('tkinter.Canvas.postscript'):
        save_button.save_image()


def test_color_button_choose_color(mock_master, mock_canvas):
    color_button = ColorButton(mock_master, mock_canvas)
    mock_canvas.set_color = MagicMock()
    with patch(
            'tkinter.colorchooser.askcolor',
            return_value=(None, '#ffffff')
         ):
        color_button.choose_color()
    mock_canvas.set_color.assert_called_once_with('#ffffff')
