from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QSlider, QVBoxLayout, \
    QFileDialog
from hPyT import *

from pyside_version.data.canvas import Canvas
from pyside_version.data.mainWindow_ui import Ui_mainWindow
from pyside_version.data.custom_toggle import AnimatedToggle
from pyside_version.data.constants import *


def handle_slider_values(value: int) -> str:
    """
    Handle the scaling of integer values provided by slider to float alternatives.

    Since sliders in PySide always return integers we need this function to
    process these integer values and convert them to float.

    For example if a slider sends number `50` to this function it will be converted
    to `0.50`.

    :returns: A string representation of the float value padded with zeros
    """
    return f'{round(value / 100, 2):0.2f}'


class PhotoEditorView(QWidget):
    # Custom signal that will be triggered each time user applies a filter.
    ValueChanged = Signal(object)

    def __init__(self):
        super().__init__()
        self.invert_toggle = None

        # Load ui
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

        self.change_title_bar_color()
        self.create_widgets()
        self.connect_signals_to_slots()

        # Set the import image screen as default page at run time
        self.ui.stackedWidget.setCurrentIndex(0)

    def create_widgets(self):
        # Black and white check box
        self.bw_toggle = AnimatedToggle(checked_color="#1f6aa5")
        self.bw_toggle.setObjectName('greyscale_toggle')
        self.bw_toggle.setChecked(False)

        self.ui.widget_bw.setLayout(QHBoxLayout())
        self.ui.widget_bw.layout().addWidget(self.bw_toggle)
        self.ui.widget_bw.layout().addWidget(QLabel('B/W'))

        # Invert color check box
        self.invert_toggle = AnimatedToggle(checked_color="#1f6aa5")
        self.invert_toggle.setObjectName('invert_color_toggle')
        self.invert_toggle.setChecked(False)

        self.ui.widget_invert.setLayout(QHBoxLayout())
        self.ui.widget_invert.layout().addWidget(self.invert_toggle)
        self.ui.widget_invert.layout().addWidget(QLabel('Invert'))

        # Add canvas
        self.canvas = Canvas()
        canvas_layout = QVBoxLayout()
        self.ui.frm_picture.setLayout(canvas_layout)
        canvas_layout.addWidget(self.canvas)

    def connect_signals_to_slots(self):
        self.slider_label_mapping = {
            # Slider name: label widget
            'slider_rotation': self.ui.lbl_rotation,
            'slider_zoom': self.ui.lbl_zoom,
            'slider_brightness': self.ui.lbl_brightness,
            'slider_viberance': self.ui.lbl_viberance,
            'slider_blur': self.ui.lbl_blur,
            'slider_contrast': self.ui.lbl_contrast
        }

        for slider in self.findChildren(QSlider):
            slider.valueChanged.connect(self.update_display_text)

        for i in range(1, 5):
            getattr(self.ui, f'btn_invert_{i}').toggled.connect(self.flip_option_selected)

        self.ui.btn_revert_1.clicked.connect(self.revert_position_settings)
        self.ui.btn_revert_2.clicked.connect(self.revert_color_settings)
        self.ui.btn_revert_3.clicked.connect(self.revert_effect_settings)

        self.bw_toggle.toggled.connect(self.color_toggle_clicked)
        self.invert_toggle.toggled.connect(self.color_toggle_clicked)

        self.ui.comboBox_effects.currentTextChanged.connect(self.effects_selected)

        self.ui.lineEdit_image_name.textChanged.connect(self.file_name_generator)
        self.ui.checkbox_jpg.toggled.connect(self.file_name_generator)
        self.ui.checkbox_png.toggled.connect(self.file_name_generator)

        self.ui.btn_open.clicked.connect(self.evt_open_explorer_clicked)
        self.ui.btn_close.clicked.connect(self.close_image)

    def update_display_text(self, value: int):
        string_float = handle_slider_values(value)
        self.slider_label_mapping.get(self.sender().objectName()).setText(string_float)
        self.ValueChanged.emit(float(string_float))

    def revert_position_settings(self):
        self.ui.slider_rotation.setValue(ROTATE_DEFAULT * 100)
        self.ui.slider_zoom.setValue(ZOOM_DEFAULT * 100)
        self.ui.btn_invert_1.setChecked(True)

    def revert_color_settings(self):
        self.bw_toggle.setChecked(False)
        self.invert_toggle.setChecked(False)
        self.ui.slider_brightness.setValue(BRIGHTNESS_DEFAULT * 100)
        self.ui.slider_viberance.setValue(VIBRANCE_DEFAULT * 100)

    def revert_effect_settings(self):
        self.ui.comboBox_effects.setCurrentIndex(0)
        self.ui.slider_blur.setValue(BLUR_DEFAULT * 100)
        self.ui.slider_contrast.setValue(CONTRAST_DEFAULT * 100)

    def reset_export_settings(self):
        self.ui.lineEdit_image_name.clear()
        self.ui.lineEdit_save_path.clear()
        self.ui.checkbox_jpg.setChecked(True)

    def flip_option_selected(self):
        button_text = self.sender().text()
        self.ValueChanged.emit(None if button_text == 'None' else button_text)

    def color_toggle_clicked(self, state: bool):
        self.ValueChanged.emit(state)

    def effects_selected(self, value: str):
        self.ValueChanged.emit(None if value == 'None' else value)

    def reset_view(self):
        self.revert_color_settings()
        self.revert_effect_settings()
        self.revert_position_settings()
        self.reset_export_settings()

    def file_name_generator(self):
        value: str = self.ui.lineEdit_image_name.text()
        extension: str = '.jpg' if self.ui.checkbox_jpg.isChecked() else '.png'
        full_name: str = f'{value.replace(' ', '_')}{extension}' if value else ''
        self.ui.lbl_full_image_name.setText(full_name)

    def evt_open_explorer_clicked(self):
        path: str = QFileDialog.getExistingDirectory(self, 'Select a folder')
        if path:
            self.ui.lineEdit_save_path.setText(path)

    def change_title_bar_color(self) -> None:
        """
        Changes the color of the title bar to black.
        Only works for the windows.

        :return: None
        """
        title_bar_color.set(self, '#242424')  # sets the titlebar color to white

    def close_image(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.reset_view()
