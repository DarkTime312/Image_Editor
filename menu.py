import customtkinter as ctk
from settings import *
from panels import RotationPanel, ZoomPanel, InvertPanel, ColorSwitches, BrightnessPanel, VibrancePanel, \
    BlurPanel, ContrastPanel
from image_widgets import ExportName, ExportFolder


class MyTabView(ctk.CTkTabview):
    def __init__(self, master, brightness_level, vibrance_level, rotation_degree, zoom_level, blur_level,
                 contrast_level, grey_scale_var, invert_var):
        super().__init__(master, fg_color=BACKGROUND_COLOR)
        self.grid(row=0, column=0, sticky='news')

        # create tabs
        position_frm = self.add("Position")
        color_frm = self.add("Color")
        effects_frm = self.add("Effects")
        export_frm = self.add("Export")

        PositionMenu(position_frm, rotation_degree, zoom_level)
        ColorMenu(color_frm, brightness_level, vibrance_level, grey_scale_var, invert_var)
        EffectsMenu(effects_frm, blur_level, contrast_level)
        ExportMenu(export_frm)


class PositionMenu(ctk.CTkFrame):
    def __init__(self, parent, rotation_degree, zoom_level):
        super().__init__(master=parent)
        self.pack(expand=True, fill='both', padx=5)

        RotationPanel(parent=self, text='Rotation', max_value=360, variable=rotation_degree)
        ZoomPanel(parent=self, text='Zoom', max_value=200, variable=zoom_level)
        InvertPanel(self)

        # RevertButton(self)


class ColorMenu(ctk.CTkFrame):
    def __init__(self, parent, brightness_level, vibrance_level, grey_scale_var, invert_var):
        super().__init__(master=parent)
        self.pack(expand=True, fill='both')

        ColorSwitches(self, grey_scale_var, invert_var)
        BrightnessPanel(parent=self, text='Brightness', max_value=5, variable=brightness_level)
        VibrancePanel(parent=self, text='Vibrance', max_value=5, variable=vibrance_level)

        RevertButton(self, ((grey_scale_var, GRAYSCALE_DEFAULT),
                            (invert_var, INVERT_DEFAULT),
                            (brightness_level, BRIGHTNESS_DEFAULT),
                            (vibrance_level, VIBRANCE_DEFAULT)
                            ))


class EffectsMenu(ctk.CTkFrame):
    def __init__(self, parent, blur_level, contrast_level):
        super().__init__(master=parent)
        self.pack(expand=True, fill='both')

        effect_options = ctk.CTkOptionMenu(self,
                                           values=EFFECT_OPTIONS,
                                           fg_color=DARK_GREY,
                                           dropdown_fg_color=DROPDOWN_MENU_COLOR,
                                           button_color=DROPDOWN_MAIN_COLOR,
                                           button_hover_color=DROPDOWN_HOVER_COLOR)
        effect_options.pack(fill='x', padx=5, pady=5)

        BlurPanel(parent=self, text='Blur', max_value=30, variable=blur_level)
        ContrastPanel(parent=self, text='Contrast', max_value=10, variable=contrast_level)

        # RevertButton(self)


class ExportMenu(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent)
        self.pack(expand=True, fill='both')

        ExportName(self)
        ExportFolder(self)
        save_btn = ctk.CTkButton(self, text='Save', width=150)
        save_btn.pack(side='bottom', pady=15)


class RevertButton(ctk.CTkButton):
    def __init__(self, parent, defaults):
        super().__init__(master=parent, text='Revert', width=150, command=lambda: self.revert(defaults))
        self.pack(side='bottom', pady=15)

    def revert(self, defaults: tuple[tuple]):
        for variable, value in defaults:
            variable.set(value)
