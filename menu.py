import customtkinter as ctk
from settings import *
from panels import RotationPanel, ZoomPanel, InvertPanel, ColorSwitches, BrightnessPanel, VibrancePanel, \
    BlurPanel, ContrastPanel
from image_widgets import ExportName, ExportFolder


class MyTabView(ctk.CTkTabview):
    def __init__(self, master):
        super().__init__(master, fg_color=BACKGROUND_COLOR)
        self.grid(row=0, column=0, sticky='news')

        # create tabs
        position_frm = self.add("Position")
        color_frm = self.add("Color")
        effects_frm = self.add("Effects")
        export_frm = self.add("Export")

        PositionMenu(position_frm)
        ColorMenu(color_frm)
        EffectsMenu(effects_frm)
        ExportMenu(export_frm)


class PositionMenu(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent)
        self.pack(expand=True, fill='both', padx=5)

        RotationPanel(parent=self, text='Rotation', max_value=360)
        ZoomPanel(parent=self, text='Zoom', max_value=200)
        InvertPanel(self)

        RevertButton(self)


class ColorMenu(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent)
        self.pack(expand=True, fill='both')

        ColorSwitches(self)
        BrightnessPanel(parent=self, text='Brightness', max_value=5)
        VibrancePanel(parent=self, text='Vibrance', max_value=5)

        RevertButton(self)


class EffectsMenu(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent)
        self.pack(expand=True, fill='both')

        effect_options = ctk.CTkOptionMenu(self,
                                           values=EFFECT_OPTIONS,
                                           fg_color=DARK_GREY,
                                           dropdown_fg_color=DROPDOWN_MENU_COLOR,
                                           button_color=DROPDOWN_MAIN_COLOR,
                                           button_hover_color=DROPDOWN_HOVER_COLOR)
        effect_options.pack(fill='x', padx=5, pady=5)

        BlurPanel(parent=self, text='Blur', max_value=30)
        ContrastPanel(parent=self, text='Contrast', max_value=10)

        RevertButton(self)


class ExportMenu(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent)
        self.pack(expand=True, fill='both')

        ExportName(self)
        ExportFolder(self)
        save_btn = ctk.CTkButton(self, text='Save', width=150)
        save_btn.pack(side='bottom', pady=15)


class RevertButton(ctk.CTkButton):
    def __init__(self, parent):
        super().__init__(master=parent, text='Revert', width=150)
        self.pack(side='bottom', pady=15)
