import os

from PIL import ImageEnhance, ImageFilter
from PySide6.QtGui import QImage, QTransform
from PySide6.QtWidgets import QFileDialog, QMessageBox

from pyside_version.MVC.model import PhotoEditorModel
from pyside_version.MVC.view import PhotoEditorView
from pyside_version.data import filters


def convert_pil_to_qimage(pil_img):
    """Convert from a pillow image to QImage"""
    im = pil_img.convert("RGB")
    data = im.tobytes("raw", "RGB")
    qi = QImage(data, im.size[0], im.size[1], im.size[0] * 3, QImage.Format.Format_RGB888)

    return qi


class PhotoEditorController:
    def __init__(self):
        self.last_qt_image = None
        self.view = PhotoEditorView()
        self.model = PhotoEditorModel()
        self.connect_signals_to_slots()

    def connect_signals_to_slots(self):
        self.view.ValueChanged.connect(self.evt_filter_selected)
        self.view.ui.btn_import_image.clicked.connect(self.import_image)
        self.view.ui.btn_save.clicked.connect(self.save_image)

    def save_image(self):
        file_name = self.view.ui.lbl_full_image_name.text()
        save_path = self.view.ui.lineEdit_save_path.text()
        if file_name and save_path:
            self.last_qt_image.save(str(os.path.join(save_path, file_name)))
            msg_box = QMessageBox(self.view)
            msg_box.setIcon(QMessageBox.Icon.Information)
            msg_box.setWindowTitle('File saved')
            msg_box.setText(f"The Image: {file_name} successfully saved in\n{save_path}")
            msg_box.setStyleSheet("color: black")
            msg_box.exec()

    def evt_filter_selected(self, value):
        self.model.update_filters(self.view.sender(), value)
        self.apply_filters()

    def import_image(self):
        filetypes = [
            "All Files (*)",
            "BMP Files (*.bmp *.dib)",
            "GIF Files (*.gif)",
            "ICO Files (*.ico)",
            "PNG Files (*.png)",
            "JPEG Files (*.jpeg *.jpg)",
        ]
        path, _ = QFileDialog.getOpenFileName(self.view, 'Select image', '', ';;'.join(filetypes))
        if path:
            self.model.set_image_path(path)
            self.model.load_pill_img()
            self.view.ui.stackedWidget.setCurrentIndex(1)
            self.view.canvas.load_image(path)

    def apply_filters(self):
        image = self.view.canvas.get_image()
        pillow_related_effects = [
            self.model.brightness_level,
            self.model.vibrance_level,
            self.model.blur_level,
            self.model.contrast_level,
            self.model.effect,
        ]

        if any(pillow_related_effects):
            image = self.model.pil_img.copy()
            if self.model.brightness_level:
                # Set brightness
                enhancer = ImageEnhance.Brightness(image)
                image = enhancer.enhance(self.model.brightness_level)

            if self.model.vibrance_level:
                # set Vibrance
                enhancer = ImageEnhance.Color(image)
                image = enhancer.enhance(self.model.vibrance_level)
            if self.model.blur_level:
                # Set Blur
                image = image.filter(ImageFilter.GaussianBlur(self.model.blur_level))
            if self.model.contrast_level:
                enhancer = ImageEnhance.Contrast(image)
                image = enhancer.enhance(self.model.contrast_level)
            if self.model.effect:
                # Apply the selected effect based on the effect_name
                image = filters.apply_effect(image, effect=self.model.effect)

            image = convert_pil_to_qimage(image)

        if self.model.flip_mode:
            image = filters.flip_image(image, flip_mode=self.model.flip_mode)

        if self.model.greyscale:
            image = image.convertToFormat(QImage.Format.Format_Grayscale8)
        if self.model.color_invert:
            image.invertPixels(QImage.InvertMode.InvertRgb)
        if self.model.rotation_degree:
            image = image.transformed(QTransform().rotate(self.model.rotation_degree))

        if self.model.zoom_level:
            image = filters.zoom_and_crop(image, self.model.zoom_level)

        self.last_qt_image = image

        self.view.canvas.display_image(image)
