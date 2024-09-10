from MVC.controller import PhotoEditorController
from PySide6.QtWidgets import QApplication
import sys

#Todo: create a Canvass
# load the image on screen
# each time a value changes apply the filters (custom signals)
# you need access to default settings use it to initialize
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PhotoEditorController()
    window.view.show()
    sys.exit(app.exec())
