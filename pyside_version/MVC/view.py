from PySide6.QtCore import QSize, Signal
from PySide6.QtGui import QFont, QPixmap, Qt
from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QSlider, QGraphicsView, QGraphicsScene, QVBoxLayout
from pyside_version.data.mainWindow_ui import Ui_mainWindow
from pyside_version.data.mark_widget import AnimatedToggle


def handle_slider_values(value: int) -> str:
    """
    Handle the scaling of integer values provided by slider to float alternatives.

    Since sliders always return integers in qt we need this function to
    process these integers and convert them to desired float.

    For example if a slider sends number `50` to this function it will be converted
    to `0.50`.

    :returns: A string representation of the float value padded with zeros
    """
    return f'{round(value / 100, 2):0.2f}'


class PhotoEditorView(QWidget):
    ValueChanged = Signal(object)

    def __init__(self):
        super().__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.add_custom_widgets()
        self.connect_signals_to_slots()
        self.create_canvass()

    def add_custom_widgets(self):
        # Black and white check box
        self.bw_toggle = AnimatedToggle(checked_color="#1f6aa5")
        self.ui.widget_bw.setLayout(QHBoxLayout())
        self.ui.widget_bw.layout().addWidget(self.bw_toggle)
        bw_label = QLabel('B/W')
        self.ui.widget_bw.layout().addWidget(bw_label)
        self.bw_toggle.setChecked(False)

        # Invert color check box
        invert_toggle = AnimatedToggle(checked_color="#1f6aa5")
        invert_toggle.setChecked(False)
        self.ui.widget_invert.setLayout(QHBoxLayout())
        self.ui.widget_invert.layout().addWidget(invert_toggle)
        self.ui.widget_invert.layout().addWidget(QLabel('Invert'))

    def connect_signals_to_slots(self):
        self.labels = {
            'slider_rotation': self.ui.lbl_rotation,
            'slider_zoom': self.ui.lbl_zoom,
            'slider_brightness': self.ui.lbl_brightness,
            'slider_viberance': self.ui.lbl_viberance,
            'slider_blur': self.ui.lbl_blur,
            'slider_contrast': self.ui.lbl_contrast
        }
        for slider in self.findChildren(QSlider):
            slider.valueChanged.connect(self.update_display_text)

    def update_display_text(self, value: int):
        self.labels.get(self.sender().objectName()).setText(handle_slider_values(value))
        self.ValueChanged.emit(handle_slider_values(value))

    def create_canvass(self):
        self.canvas = Canvas()
        # self.canvas.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.canvas.setStyleSheet("background-color: transparent")
        canvas_layout = QVBoxLayout()
        self.ui.frm_picture.setLayout(canvas_layout)
        canvas_layout.addWidget(self.canvas)
        self.canvas.load_image(r'C:\Users\rozes\OneDrive\Pictures\b0fbnuew8zcd1.jpeg')


class Canvas(QGraphicsView):
    def __init__(self):
        super().__init__()

        # Create a scene
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)

        # Enable resizing
        self.setResizeAnchor(QGraphicsView.ViewportAnchor.AnchorViewCenter)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.pixmap_item = None  # Placeholder for the pixmap item

    def load_image(self, image_path):
        # Load the image
        pixmap = QPixmap(image_path)

        # Clear the scene before adding a new pixmap
        self.scene.clear()

        # Add the pixmap to the scene
        self.pixmap_item = self.scene.addPixmap(pixmap)

        # Set scene rectangle to match the pixmap size
        self.scene.setSceneRect(pixmap.rect())

    def resizeEvent(self, event):
        super().resizeEvent(event)
        if self.pixmap_item:
            self.fitInView(self.pixmap_item, Qt.AspectRatioMode.KeepAspectRatio)
