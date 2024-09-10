from pyside_version.MVC.view import PhotoEditorView
from pyside_version.MVC.model import PhotoEditorModel


class PhotoEditorController:
    def __init__(self):
        self.view = PhotoEditorView()
        self.model = PhotoEditorModel()
        self.connect_signals_to_slots()

    def connect_signals_to_slots(self):
        self.view.ValueChanged.connect(self.test)

    def test(self, value):
        print(self.view.sender(), value)
