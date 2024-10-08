from typing import Any

from PIL import Image
from PySide6.QtCore import QObject

from pyside_version.data.constants import *


class PhotoEditorModel:
    def __init__(self):
        self.pil_img = None
        self.rotation_degree = None
        self.zoom_level = None
        self.brightness_level = None
        self.vibrance_level = None
        self.blur_level = None
        self.contrast_level = None
        self.flip_mode = None
        self.greyscale = None
        self.color_invert = None
        self.effect = None

        self.data = {
            # Object name: (attribute, default value)
            'slider_rotation': ('rotation_degree', ROTATE_DEFAULT),
            'slider_zoom': ('zoom_level', ZOOM_DEFAULT),
            'slider_brightness': ('brightness_level', BRIGHTNESS_DEFAULT),
            'slider_viberance': ('vibrance_level', VIBRANCE_DEFAULT),
            'slider_blur': ('blur_level', BLUR_DEFAULT),
            'slider_contrast': ('contrast_level', CONTRAST_DEFAULT),
            'btn_invert_1': ('flip_mode', FLIP_MODE_DEFAULT),
            'btn_invert_2': ('flip_mode', FLIP_MODE_DEFAULT),
            'btn_invert_3': ('flip_mode', FLIP_MODE_DEFAULT),
            'btn_invert_4': ('flip_mode', FLIP_MODE_DEFAULT),
            'greyscale_toggle': ('greyscale', GRAYSCALE_DEFAULT),
            'invert_color_toggle': ('color_invert', INVERT_DEFAULT),
            'comboBox_effects': ('effect', EFFECTS_DEFAULT),
        }

    def load_pil_img(self, path: str):
        self.pil_img = Image.open(path)

        if self.pil_img.mode != 'RGB':
            self.pil_img = self.pil_img.convert('RGB')

    def update_filters(self, sender_object: QObject, value: Any):
        attribute, default_value = self.data.get(sender_object.objectName())
        setattr(self, attribute, None if value == default_value else value)
