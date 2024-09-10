from PySide6.QtWidgets import QFileDialog

from pyside_version.MVC.view import PhotoEditorView
from pyside_version.MVC.model import PhotoEditorModel


class PhotoEditorController:
    def __init__(self):
        self.view = PhotoEditorView()
        self.model = PhotoEditorModel()
        self.connect_signals_to_slots()

    def connect_signals_to_slots(self):
        self.view.ValueChanged.connect(self.test)
        self.view.ui.btn_import_image.clicked.connect(self.import_image)
        self.view.ui.btn_close.clicked.connect(self.close_image)

    def test(self, value):
        print(self.view.sender(), value)
        self.model.update_filters(self.view.sender(), value)

    def import_image(self):
        filetypes = [
            "All Image Files (*.bmp *.dib *.eps *.gif *.icns *.ico *.im *.jpeg *.jpg *.msp *.pcx *.png *.ppm *.pgm "
            "*.pbm *.sgi *.spider *.tga *.tiff *.tif *.webp *.xbm *.xpm)",
            "BMP Files (*.bmp *.dib)",
            "EPS Files (*.eps)",
            "GIF Files (*.gif)",
            "ICNS Files (*.icns)",
            "ICO Files (*.ico)",
            "IM Files (*.im)",
            "PNG Files (*.png)",
            "JPEG Files (*.jpeg *.jpg)",
        ]
        path, _ = QFileDialog.getOpenFileName(self.view, 'Select image', '', ';;'.join(filetypes))
        if path:
            self.model.set_image_path(path)
            self.view.ui.stackedWidget.setCurrentIndex(1)
            self.view.canvas.load_image(path)

    def close_image(self):
        self.view.ui.stackedWidget.setCurrentIndex(0)
        self.view.reset_view()
