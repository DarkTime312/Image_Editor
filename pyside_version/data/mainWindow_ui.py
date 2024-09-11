# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
                               QHBoxLayout, QLabel, QLineEdit, QPushButton,
                               QSizePolicy, QSlider, QSpacerItem, QStackedWidget,
                               QTabWidget, QVBoxLayout, QWidget)
from pyside_version.data import resource_rc


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(1000, 600)
        mainWindow.setMinimumSize(QSize(800, 500))
        icon = QIcon()
        icon.addFile(u":/assets/icon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        mainWindow.setWindowIcon(icon)
        mainWindow.setStyleSheet(u"QWidget#mainWindow {\n"
                                 "background-color: #242424\n"
                                 "}\n"
                                 "QWidget#tab,\n"
                                 "QWidget#tab_2,\n"
                                 "QWidget#tab_3,\n"
                                 "QWidget#tab_4 {\n"
                                 "background-color: #2b2b2b\n"
                                 "}\n"
                                 "QWidget#mainWindow {\n"
                                 "background-color: #242424\n"
                                 "}\n"
                                 "\n"
                                 "QStackedWidget {\n"
                                 "	background-color: #242424;\n"
                                 "}\n"
                                 "\n"
                                 "QWidget#page_import, QWidget#page_main {\n"
                                 "background-color: transparent\n"
                                 "}\n"
                                 " /* Buttons */\n"
                                 "QPushButton#btn_revert_1,\n"
                                 "QPushButton#btn_revert_2,\n"
                                 "QPushButton#btn_revert_3,\n"
                                 "QPushButton#btn_revert_4,\n"
                                 "QPushButton#btn_open,\n"
                                 " QPushButton#btn_save,\n"
                                 " QPushButton#btn_import_image {\n"
                                 "	background-color: #1f6aa5;\n"
                                 "	color: white;\n"
                                 "    min-width: 150px; \n"
                                 "    min-height: 30px;  \n"
                                 "    max-width: 150px; \n"
                                 "    max-height: 30px;  \n"
                                 "	border: 1px solid transparent;\n"
                                 "	border-radius: 5px\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton#btn_revert_1:hover,\n"
                                 "QPushButton#btn_revert_2:hover,\n"
                                 "QPushButton#btn_revert_3:hover,\n"
                                 "QPushButton#btn_revert_4:hover,\n"
                                 "QPushButton#btn_open:hover,\n"
                                 " Q"
                                 "PushButton#btn_save:hover,\n"
                                 " QPushButton#btn_import_image:hover {\n"
                                 "	background-color: #144870;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton#btn_revert_1:pressed,\n"
                                 "QPushButton#btn_revert_2:pressed,\n"
                                 "QPushButton#btn_revert_3:pressed,\n"
                                 "QPushButton#btn_revert_4:pressed,\n"
                                 "QPushButton#btn_open:pressed,\n"
                                 " QPushButton#btn_save:pressed,\n"
                                 " QPushButton#btn_import_image:pressed  {\n"
                                 "	background-color: #1f6aa5;\n"
                                 "}\n"
                                 " /* Invert Buttons */\n"
                                 "QPushButton#btn_invert_1,\n"
                                 "QPushButton#btn_invert_2,\n"
                                 "QPushButton#btn_invert_3,\n"
                                 "QPushButton#btn_invert_4 {\n"
                                 "    min-width: 40px; \n"
                                 "    min-height: 30px;  \n"
                                 "	color: white;\n"
                                 "	border: 1px solid transparent;\n"
                                 "	background-color: transparent\n"
                                 "}\n"
                                 "QPushButton#btn_invert_1:checked,\n"
                                 "QPushButton#btn_invert_2:checked,\n"
                                 "QPushButton#btn_invert_3:checked,\n"
                                 "QPushButton#btn_invert_4:checked {\n"
                                 "	background-color: #1f6aa5;\n"
                                 "	border: 1px solid transparent;\n"
                                 "	border-radius: 5px\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton#btn_invert_1:checked:hover,\n"
                                 "QPushBut"
                                 "ton#btn_invert_2:checked:hover,\n"
                                 "QPushButton#btn_invert_3:checked:hover,\n"
                                 "QPushButton#btn_invert_4:checked:hover {\n"
                                 "	background-color: #144870;\n"
                                 "	border: 1px solid transparent;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton#btn_invert_1:!checked:hover,\n"
                                 "QPushButton#btn_invert_2:!checked:hover,\n"
                                 "QPushButton#btn_invert_3:!checked:hover,\n"
                                 "QPushButton#btn_invert_4:!checked:hover {\n"
                                 "	background-color: #696969;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton#btn_close {\n"
                                 "	background-color: transparent;\n"
                                 "}\n"
                                 "QPushButton#btn_close:hover {\n"
                                 "	background-color: #8a0606;\n"
                                 "}\n"
                                 " /* Tab headers */\n"
                                 "\n"
                                 "QTabWidget{\n"
                                 "	background-color: #2b2b2b\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "\n"
                                 "QTabBar{\n"
                                 "	background-color: #4a4a4a;\n"
                                 "	border: 1px solid transparent;\n"
                                 "	color: white;\n"
                                 "	border-radius: 5px;\n"
                                 "\n"
                                 "}\n"
                                 "QTabWidget::tab-bar {\n"
                                 "    alignment: center;\n"
                                 "}\n"
                                 "\n"
                                 "QTabBar::tab:selected {\n"
                                 "    background: #1f6aa5;;\n"
                                 "	padding: 3px 7px;\n"
                                 "	border: 1px solid transparent;\n"
                                 "	border-radius: 5px;\n"
                                 "\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 ""
                                 "QTabBar::tab {\n"
                                 "    background: #4a4a4a; \n"
                                 "    color: white; \n"
                                 "	border: 1px solid transparent;\n"
                                 "	border-radius: 5px;\n"
                                 "	padding: 3px 7px;\n"
                                 "\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 " \n"
                                 "QTabBar::tab:hover {\n"
                                 "    background: #144870; \n"
                                 "}\n"
                                 "\n"
                                 "QFrame#frm_rotation,\n"
                                 "QFrame#frm_zoom,\n"
                                 "QFrame#frm_invert,\n"
                                 "QFrame#frm_blur,\n"
                                 "QFrame#frm_contrast,\n"
                                 "QFrame#frm_toggles,\n"
                                 "QFrame#frm_brightness,\n"
                                 "QFrame#frm_viberance,\n"
                                 "QFrame#frm_file_name,\n"
                                 "QFrame#frm_save_path{\n"
                                 "	background-color: #4a4a4a;\n"
                                 "	border: 1px solid transparent;\n"
                                 "	border-radius: 5px\n"
                                 "}\n"
                                 "QFrame#frm_picture,\n"
                                 "QFrame#frm_right_side{\n"
                                 "	background-color: #242424;\n"
                                 "}\n"
                                 "QLabel{\n"
                                 "color: white\n"
                                 "}\n"
                                 " /* Combo box */\n"
                                 "\n"
                                 "QComboBox{\n"
                                 "	background-color: #4a4a4a;\n"
                                 "	color: white;\n"
                                 "	padding: 5px 10px;\n"
                                 "	border: 1px solid transparent;\n"
                                 "	border-radius: 10px\n"
                                 "}\n"
                                 "\n"
                                 "QComboBox QAbstractItemView {\n"
                                 "    background-color: #666;  /* Background color of the dropdown list */\n"
                                 "	color: whi"
                                 "te;\n"
                                 "    border: 2px solid white;      /* Border of the dropdown list */\n"
                                 "    selection-background-color: #474747; /* Background color of selected item */\n"
                                 "    selection-color: white;      /* Text color of selected item */\n"
                                 "}\n"
                                 "\n"
                                 "QLineEdit{\n"
                                 "	background-color: #343638;\n"
                                 "	color: white\n"
                                 "}\n"
                                 "QCheckBox{\n"
                                 "	color: white;\n"
                                 "	background-color: transparent\n"
                                 "}\n"
                                 "\n"
                                 "QCheckBox::indicator:unchecked {\n"
                                 "                width: 28px;  /* Width of the indicator */\n"
                                 "                height: 28px; /* Height of the indicator */\n"
                                 "	 image: url(:/assets/checkbox.png)\n"
                                 "            }\n"
                                 "QCheckBox::indicator:checked {\n"
                                 "     image: url(:/assets/checkbox-checked-pressed.png);\n"
                                 "}\n"
                                 "\n"
                                 "")
        self.verticalLayout = QVBoxLayout(mainWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = QStackedWidget(mainWindow)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_import = QWidget()
        self.page_import.setObjectName(u"page_import")
        self.verticalLayout_2 = QVBoxLayout(self.page_import)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btn_import_image = QPushButton(self.page_import)
        self.btn_import_image.setObjectName(u"btn_import_image")
        self.btn_import_image.setMinimumSize(QSize(152, 32))
        font = QFont()
        font.setStyleStrategy(QFont.PreferAntialias)
        font.setHintingPreference(QFont.PreferNoHinting)
        self.btn_import_image.setFont(font)

        self.verticalLayout_2.addWidget(self.btn_import_image, 0, Qt.AlignmentFlag.AlignHCenter)

        self.stackedWidget.addWidget(self.page_import)
        self.page_main = QWidget()
        self.page_main.setObjectName(u"page_main")
        self.horizontalLayout_2 = QHBoxLayout(self.page_main)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.page_main)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setFont(font)
        self.tabWidget.setTabShape(QTabWidget.TabShape.Rounded)
        self.tabWidget.setElideMode(Qt.TextElideMode.ElideLeft)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setFont(font)
        self.verticalLayout_3 = QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frm_rotation = QFrame(self.tab)
        self.frm_rotation.setObjectName(u"frm_rotation")
        self.frm_rotation.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_rotation.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frm_rotation)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.frm_rotation)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.horizontalLayout_3.addWidget(self.label)

        self.lbl_rotation = QLabel(self.frm_rotation)
        self.lbl_rotation.setObjectName(u"lbl_rotation")
        self.lbl_rotation.setFont(font)
        self.lbl_rotation.setAlignment(
            Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTrailing | Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.lbl_rotation)

        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.slider_rotation = QSlider(self.frm_rotation)
        self.slider_rotation.setObjectName(u"slider_rotation")
        self.slider_rotation.setMaximum(36000)
        self.slider_rotation.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_4.addWidget(self.slider_rotation)

        self.verticalLayout_3.addWidget(self.frm_rotation)

        self.frm_zoom = QFrame(self.tab)
        self.frm_zoom.setObjectName(u"frm_zoom")
        self.frm_zoom.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_zoom.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frm_zoom)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.frm_zoom)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_3)

        self.lbl_zoom = QLabel(self.frm_zoom)
        self.lbl_zoom.setObjectName(u"lbl_zoom")
        self.lbl_zoom.setFont(font)
        self.lbl_zoom.setAlignment(
            Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTrailing | Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.lbl_zoom)

        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.slider_zoom = QSlider(self.frm_zoom)
        self.slider_zoom.setObjectName(u"slider_zoom")
        self.slider_zoom.setMinimum(100)
        self.slider_zoom.setMaximum(500)
        self.slider_zoom.setValue(100)
        self.slider_zoom.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_5.addWidget(self.slider_zoom)

        self.verticalLayout_3.addWidget(self.frm_zoom)

        self.frm_invert = QFrame(self.tab)
        self.frm_invert.setObjectName(u"frm_invert")
        self.frm_invert.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_invert.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frm_invert)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_5 = QLabel(self.frm_invert)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_5)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.btn_invert_1 = QPushButton(self.frm_invert)
        self.btn_invert_1.setObjectName(u"btn_invert_1")
        self.btn_invert_1.setFont(font)
        self.btn_invert_1.setCheckable(True)
        self.btn_invert_1.setChecked(True)
        self.btn_invert_1.setAutoExclusive(True)
        self.btn_invert_1.setFlat(False)

        self.horizontalLayout_5.addWidget(self.btn_invert_1)

        self.btn_invert_2 = QPushButton(self.frm_invert)
        self.btn_invert_2.setObjectName(u"btn_invert_2")
        self.btn_invert_2.setFont(font)
        self.btn_invert_2.setCheckable(True)
        self.btn_invert_2.setAutoExclusive(True)
        self.btn_invert_2.setFlat(True)

        self.horizontalLayout_5.addWidget(self.btn_invert_2)

        self.btn_invert_3 = QPushButton(self.frm_invert)
        self.btn_invert_3.setObjectName(u"btn_invert_3")
        self.btn_invert_3.setFont(font)
        self.btn_invert_3.setCheckable(True)
        self.btn_invert_3.setChecked(False)
        self.btn_invert_3.setAutoExclusive(True)
        self.btn_invert_3.setFlat(True)

        self.horizontalLayout_5.addWidget(self.btn_invert_3)

        self.btn_invert_4 = QPushButton(self.frm_invert)
        self.btn_invert_4.setObjectName(u"btn_invert_4")
        self.btn_invert_4.setFont(font)
        self.btn_invert_4.setCheckable(True)
        self.btn_invert_4.setAutoExclusive(True)
        self.btn_invert_4.setFlat(True)

        self.horizontalLayout_5.addWidget(self.btn_invert_4)

        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.verticalLayout_3.addWidget(self.frm_invert)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.btn_revert_1 = QPushButton(self.tab)
        self.btn_revert_1.setObjectName(u"btn_revert_1")
        self.btn_revert_1.setFont(font)

        self.verticalLayout_3.addWidget(self.btn_revert_1, 0, Qt.AlignmentFlag.AlignHCenter)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tab_2.setFont(font)
        self.verticalLayout_10 = QVBoxLayout(self.tab_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frm_toggles = QFrame(self.tab_2)
        self.frm_toggles.setObjectName(u"frm_toggles")
        self.frm_toggles.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_toggles.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frm_toggles)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.widget_bw = QWidget(self.frm_toggles)
        self.widget_bw.setObjectName(u"widget_bw")

        self.horizontalLayout_8.addWidget(self.widget_bw)

        self.widget_invert = QWidget(self.frm_toggles)
        self.widget_invert.setObjectName(u"widget_invert")
        self.widget_invert.setMinimumSize(QSize(50, 50))

        self.horizontalLayout_8.addWidget(self.widget_invert)

        self.verticalLayout_10.addWidget(self.frm_toggles)

        self.frm_brightness = QFrame(self.tab_2)
        self.frm_brightness.setObjectName(u"frm_brightness")
        self.frm_brightness.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_brightness.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frm_brightness)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_10 = QLabel(self.frm_brightness)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)

        self.horizontalLayout_10.addWidget(self.label_10)

        self.lbl_brightness = QLabel(self.frm_brightness)
        self.lbl_brightness.setObjectName(u"lbl_brightness")
        self.lbl_brightness.setFont(font)
        self.lbl_brightness.setAlignment(
            Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTrailing | Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.lbl_brightness)

        self.verticalLayout_12.addLayout(self.horizontalLayout_10)

        self.slider_brightness = QSlider(self.frm_brightness)
        self.slider_brightness.setObjectName(u"slider_brightness")
        self.slider_brightness.setMinimum(0)
        self.slider_brightness.setMaximum(500)
        self.slider_brightness.setValue(100)
        self.slider_brightness.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_12.addWidget(self.slider_brightness)

        self.verticalLayout_10.addWidget(self.frm_brightness)

        self.frm_viberance = QFrame(self.tab_2)
        self.frm_viberance.setObjectName(u"frm_viberance")
        self.frm_viberance.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_viberance.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frm_viberance)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_12 = QLabel(self.frm_viberance)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)

        self.horizontalLayout_9.addWidget(self.label_12)

        self.lbl_viberance = QLabel(self.frm_viberance)
        self.lbl_viberance.setObjectName(u"lbl_viberance")
        self.lbl_viberance.setFont(font)
        self.lbl_viberance.setAlignment(
            Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTrailing | Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.lbl_viberance)

        self.verticalLayout_11.addLayout(self.horizontalLayout_9)

        self.slider_viberance = QSlider(self.frm_viberance)
        self.slider_viberance.setObjectName(u"slider_viberance")
        self.slider_viberance.setMaximum(500)
        self.slider_viberance.setValue(100)
        self.slider_viberance.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_11.addWidget(self.slider_viberance)

        self.verticalLayout_10.addWidget(self.frm_viberance)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_3)

        self.btn_revert_2 = QPushButton(self.tab_2)
        self.btn_revert_2.setObjectName(u"btn_revert_2")
        self.btn_revert_2.setFont(font)

        self.verticalLayout_10.addWidget(self.btn_revert_2, 0, Qt.AlignmentFlag.AlignHCenter)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tab_3.setFont(font)
        self.verticalLayout_7 = QVBoxLayout(self.tab_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.comboBox_effects = QComboBox(self.tab_3)
        self.comboBox_effects.addItem("")
        self.comboBox_effects.addItem("")
        self.comboBox_effects.addItem("")
        self.comboBox_effects.addItem("")
        self.comboBox_effects.addItem("")
        self.comboBox_effects.setObjectName(u"comboBox_effects")
        self.comboBox_effects.setMinimumSize(QSize(0, 30))
        self.comboBox_effects.setFont(font)

        self.verticalLayout_7.addWidget(self.comboBox_effects)

        self.frm_blur = QFrame(self.tab_3)
        self.frm_blur.setObjectName(u"frm_blur")
        self.frm_blur.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_blur.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frm_blur)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.frm_blur)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.horizontalLayout_6.addWidget(self.label_6)

        self.lbl_blur = QLabel(self.frm_blur)
        self.lbl_blur.setObjectName(u"lbl_blur")
        self.lbl_blur.setFont(font)
        self.lbl_blur.setAlignment(
            Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTrailing | Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.lbl_blur)

        self.verticalLayout_8.addLayout(self.horizontalLayout_6)

        self.slider_blur = QSlider(self.frm_blur)
        self.slider_blur.setObjectName(u"slider_blur")
        self.slider_blur.setMaximum(3000)
        self.slider_blur.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_8.addWidget(self.slider_blur)

        self.verticalLayout_7.addWidget(self.frm_blur)

        self.frm_contrast = QFrame(self.tab_3)
        self.frm_contrast.setObjectName(u"frm_contrast")
        self.frm_contrast.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_contrast.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frm_contrast)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_8 = QLabel(self.frm_contrast)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.horizontalLayout_7.addWidget(self.label_8)

        self.lbl_contrast = QLabel(self.frm_contrast)
        self.lbl_contrast.setObjectName(u"lbl_contrast")
        self.lbl_contrast.setFont(font)
        self.lbl_contrast.setAlignment(
            Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTrailing | Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.lbl_contrast)

        self.verticalLayout_9.addLayout(self.horizontalLayout_7)

        self.slider_contrast = QSlider(self.frm_contrast)
        self.slider_contrast.setObjectName(u"slider_contrast")
        self.slider_contrast.setMinimum(50)
        self.slider_contrast.setMaximum(1000)
        self.slider_contrast.setValue(100)
        self.slider_contrast.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_9.addWidget(self.slider_contrast)

        self.verticalLayout_7.addWidget(self.frm_contrast)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)

        self.btn_revert_3 = QPushButton(self.tab_3)
        self.btn_revert_3.setObjectName(u"btn_revert_3")
        self.btn_revert_3.setFont(font)

        self.verticalLayout_7.addWidget(self.btn_revert_3, 0, Qt.AlignmentFlag.AlignHCenter)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tab_4.setFont(font)
        self.verticalLayout_13 = QVBoxLayout(self.tab_4)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frm_file_name = QFrame(self.tab_4)
        self.frm_file_name.setObjectName(u"frm_file_name")
        self.frm_file_name.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_file_name.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frm_file_name)
        self.verticalLayout_14.setSpacing(12)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.lineEdit_image_name = QLineEdit(self.frm_file_name)
        self.lineEdit_image_name.setObjectName(u"lineEdit_image_name")

        self.verticalLayout_14.addWidget(self.lineEdit_image_name)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(9)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.checkbox_jpg = QCheckBox(self.frm_file_name)
        self.checkbox_jpg.setObjectName(u"checkbox_jpg")
        self.checkbox_jpg.setChecked(True)
        self.checkbox_jpg.setAutoExclusive(True)

        self.horizontalLayout_11.addWidget(self.checkbox_jpg)

        self.checkbox_png = QCheckBox(self.frm_file_name)
        self.checkbox_png.setObjectName(u"checkbox_png")
        self.checkbox_png.setChecked(False)
        self.checkbox_png.setAutoExclusive(True)

        self.horizontalLayout_11.addWidget(self.checkbox_png)

        self.verticalLayout_14.addLayout(self.horizontalLayout_11)

        self.lbl_full_image_name = QLabel(self.frm_file_name)
        self.lbl_full_image_name.setObjectName(u"lbl_full_image_name")
        self.lbl_full_image_name.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_14.addWidget(self.lbl_full_image_name)

        self.verticalLayout_13.addWidget(self.frm_file_name)

        self.frm_save_path = QFrame(self.tab_4)
        self.frm_save_path.setObjectName(u"frm_save_path")
        self.frm_save_path.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_save_path.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frm_save_path)
        self.verticalLayout_15.setSpacing(20)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.btn_open = QPushButton(self.frm_save_path)
        self.btn_open.setObjectName(u"btn_open")

        self.verticalLayout_15.addWidget(self.btn_open, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit_save_path = QLineEdit(self.frm_save_path)
        self.lineEdit_save_path.setObjectName(u"lineEdit_save_path")

        self.verticalLayout_15.addWidget(self.lineEdit_save_path)

        self.verticalLayout_13.addWidget(self.frm_save_path)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_4)

        self.btn_save = QPushButton(self.tab_4)
        self.btn_save.setObjectName(u"btn_save")

        self.verticalLayout_13.addWidget(self.btn_save, 0, Qt.AlignmentFlag.AlignHCenter)

        self.tabWidget.addTab(self.tab_4, "")

        self.horizontalLayout_2.addWidget(self.tabWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frm_right_side = QFrame(self.page_main)
        self.frm_right_side.setObjectName(u"frm_right_side")
        self.frm_right_side.setFrameShape(QFrame.Shape.NoFrame)
        self.frm_right_side.setFrameShadow(QFrame.Shadow.Plain)
        self.frm_right_side.setLineWidth(0)
        self.verticalLayout_16 = QVBoxLayout(self.frm_right_side)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.btn_close = QPushButton(self.frm_right_side)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(0, 0))
        self.btn_close.setMaximumSize(QSize(25, 25))
        icon1 = QIcon(QIcon.fromTheme(u"window-close"))
        self.btn_close.setIcon(icon1)

        self.verticalLayout_16.addWidget(self.btn_close, 0, Qt.AlignmentFlag.AlignRight)

        self.frm_picture = QFrame(self.frm_right_side)
        self.frm_picture.setObjectName(u"frm_picture")
        self.frm_picture.setFrameShape(QFrame.Shape.StyledPanel)
        self.frm_picture.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_16.addWidget(self.frm_picture)

        self.horizontalLayout.addWidget(self.frm_right_side)

        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 3)
        self.stackedWidget.addWidget(self.page_main)

        self.verticalLayout.addWidget(self.stackedWidget)

        self.retranslateUi(mainWindow)

        self.stackedWidget.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)
        self.btn_invert_1.setDefault(True)

        QMetaObject.connectSlotsByName(mainWindow)

    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"Photo Editor", None))
        self.btn_import_image.setText(QCoreApplication.translate("mainWindow", u"Open image", None))
        self.label.setText(QCoreApplication.translate("mainWindow", u"Rotation", None))
        self.lbl_rotation.setText(QCoreApplication.translate("mainWindow", u"0.0", None))
        self.label_3.setText(QCoreApplication.translate("mainWindow", u"Zoom", None))
        self.lbl_zoom.setText(QCoreApplication.translate("mainWindow", u"1.0", None))
        self.label_5.setText(QCoreApplication.translate("mainWindow", u"Invert", None))
        self.btn_invert_1.setText(QCoreApplication.translate("mainWindow", u"None", None))
        self.btn_invert_2.setText(QCoreApplication.translate("mainWindow", u"X", None))
        self.btn_invert_3.setText(QCoreApplication.translate("mainWindow", u"Y", None))
        self.btn_invert_4.setText(QCoreApplication.translate("mainWindow", u"Both", None))
        self.btn_revert_1.setText(QCoreApplication.translate("mainWindow", u"Revert", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab),
                                  QCoreApplication.translate("mainWindow", u"Position", None))
        self.label_10.setText(QCoreApplication.translate("mainWindow", u"Brightness", None))
        self.lbl_brightness.setText(QCoreApplication.translate("mainWindow", u"1.0", None))
        self.label_12.setText(QCoreApplication.translate("mainWindow", u"Viberance", None))
        self.lbl_viberance.setText(QCoreApplication.translate("mainWindow", u"1.0", None))
        self.btn_revert_2.setText(QCoreApplication.translate("mainWindow", u"Revert", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2),
                                  QCoreApplication.translate("mainWindow", u"Color", None))
        self.comboBox_effects.setItemText(0, QCoreApplication.translate("mainWindow", u"None", None))
        self.comboBox_effects.setItemText(1, QCoreApplication.translate("mainWindow", u"Emboss", None))
        self.comboBox_effects.setItemText(2, QCoreApplication.translate("mainWindow", u"Find edges", None))
        self.comboBox_effects.setItemText(3, QCoreApplication.translate("mainWindow", u"Contour", None))
        self.comboBox_effects.setItemText(4, QCoreApplication.translate("mainWindow", u"Edge enhance", None))

        self.label_6.setText(QCoreApplication.translate("mainWindow", u"Blur", None))
        self.lbl_blur.setText(QCoreApplication.translate("mainWindow", u"0.0", None))
        self.label_8.setText(QCoreApplication.translate("mainWindow", u"Contrast", None))
        self.lbl_contrast.setText(QCoreApplication.translate("mainWindow", u"1.0", None))
        self.btn_revert_3.setText(QCoreApplication.translate("mainWindow", u"Revert", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3),
                                  QCoreApplication.translate("mainWindow", u"Effects", None))
        self.checkbox_jpg.setText(QCoreApplication.translate("mainWindow", u"jpg", None))
        self.checkbox_png.setText(QCoreApplication.translate("mainWindow", u"png", None))
        self.lbl_full_image_name.setText("")
        self.btn_open.setText(QCoreApplication.translate("mainWindow", u"Open Explorer", None))
        self.btn_save.setText(QCoreApplication.translate("mainWindow", u"Save", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4),
                                  QCoreApplication.translate("mainWindow", u"Export", None))
        self.btn_close.setText("")
    # retranslateUi
