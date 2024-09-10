from PySide6.QtCore import QSize
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel
from pyside_version.data.mainWindow_ui import Ui_mainWindow
from pyside_version.data.mark_widget import AnimatedToggle


class PhotoEditorView(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.add_custom_widgets()

    def add_custom_widgets(self):
        # Black and white check box
        self.bw_toggle = AnimatedToggle(checked_color="#1f6aa5")
        # self.bw_toggle.setText('B/W')
        self.ui.widget_bw.setLayout(QHBoxLayout())
        self.ui.widget_bw.layout().addWidget(self.bw_toggle)
        bw_label = QLabel('B/W')
        self.ui.widget_bw.layout().addWidget(bw_label)
        self.bw_toggle.setChecked(False)
        # print(self.bw_toggle.isChecked())


        # Invert color check box
        invert_toggle = AnimatedToggle(checked_color="#1f6aa5")
        invert_toggle.setChecked(False)
        # invert_toggle.setText('Invert')
        self.ui.widget_invert.setLayout(QHBoxLayout())
        self.ui.widget_invert.layout().addWidget(invert_toggle)
        self.ui.widget_invert.layout().addWidget(QLabel('Invert'))
