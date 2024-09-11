from MVC.controller import PhotoEditorController
from PySide6.QtWidgets import QApplication
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PhotoEditorController()
    window.view.show()
    sys.exit(app.exec())
