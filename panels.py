import customtkinter as ctk
from settings import *


class SliderPanel(ctk.CTkFrame):
    def __init__(self, parent, text, max_value):
        super().__init__(master=parent, fg_color=DARK_GREY)
        self.text = text
        self.max_value = max_value
        self.pack(fill='x', padx=5, pady=5)

        self.set_layout()
        self.create_widgets()

    def set_layout(self):
        self.rowconfigure((0, 1), weight=1, uniform='a')
        self.columnconfigure((0, 1), weight=1, uniform='b')

    def create_widgets(self):
        title_label = ctk.CTkLabel(self, text=self.text)
        title_label.grid(row=0, column=0, sticky='w', padx=5, pady=5)

        zoom_level_label = ctk.CTkLabel(self, text='0.0')
        zoom_level_label.grid(row=0, column=1, sticky='e', padx=5, pady=5)

        zoom_level_slider = ctk.CTkSlider(self, from_=0, to=self.max_value, fg_color=SLIDER_BG)
        zoom_level_slider.grid(row=1, column=0, columnspan=2, sticky='ew', padx=5, pady=5)


class RotationPanel(SliderPanel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class ZoomPanel(SliderPanel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class InvertPanel(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color=DARK_GREY)
        self.pack(fill='x', padx=5, pady=5)

        self.set_layout()
        self.create_widgets()

    def set_layout(self):
        self.rowconfigure((0, 1), weight=1, uniform='a')
        self.columnconfigure((0, 1, 2, 3), weight=1, uniform='b')

    def create_widgets(self):
        title_label = ctk.CTkLabel(self, text='Invert')
        title_label.grid(row=0, column=1, columnspan=2)

        none_btn = ctk.CTkButton(self, text='None', fg_color=DARK_GREY, hover_color=GREY)
        none_btn.grid(row=1, column=0, padx=2, pady=5)

        x_btn = ctk.CTkButton(self, text='X', fg_color=DARK_GREY, hover_color=GREY)
        x_btn.grid(row=1, column=1, padx=2, pady=5)

        y_btn = ctk.CTkButton(self, text='Y', fg_color=DARK_GREY, hover_color=GREY)
        y_btn.grid(row=1, column=2, padx=2, pady=5)

        y_btn = ctk.CTkButton(self, text='Both', fg_color=DARK_GREY, hover_color=GREY)
        y_btn.grid(row=1, column=3, padx=2, pady=5)


class ColorSwitches(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color=DARK_GREY)
        self.pack(padx=5, pady=5, fill='x')

        self.set_layout()
        self.create_widgets()

    def set_layout(self):
        self.rowconfigure(0, weight=1, uniform='a')
        self.columnconfigure((0, 1), weight=1, uniform='b')

    def create_widgets(self):
        black_or_white_switch = ctk.CTkSwitch(self, text='B/W', height=50, button_color=BLUE, fg_color=GREY)
        black_or_white_switch.grid(row=0, column=0, padx=5)

        invert_color_switch = ctk.CTkSwitch(self, text='Invert', height=50, button_color=BLUE, fg_color=GREY)
        invert_color_switch.grid(row=0, column=1, padx=5)


class BrightnessPanel(SliderPanel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class VibrancePanel(SliderPanel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class BlurPanel(SliderPanel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class ContrastPanel(SliderPanel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
