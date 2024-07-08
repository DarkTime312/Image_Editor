import customtkinter as ctk
from settings import *


class SliderPanel(ctk.CTkFrame):
    def __init__(self, parent, text, max_value, variable=None):
        super().__init__(master=parent, fg_color=DARK_GREY)
        self.text = text
        self.max_value = max_value
        self.variable = variable
        self.pack(fill='x', padx=5, pady=5)

        self.set_layout()
        self.create_widgets()
        self.variable.trace('w', self.update_label)
        self.update_label()

    def set_layout(self):
        self.rowconfigure((0, 1), weight=1, uniform='a')
        self.columnconfigure((0, 1), weight=1, uniform='b')

    def create_widgets(self):
        title_label = ctk.CTkLabel(self, text=self.text)
        title_label.grid(row=0, column=0, sticky='w', padx=5, pady=5)

        self.slide_value_indicator = ctk.CTkLabel(self)
        self.slide_value_indicator.grid(row=0, column=1, sticky='e', padx=5, pady=5)

        slider = ctk.CTkSlider(self,
                               from_=0,
                               to=self.max_value,
                               fg_color=SLIDER_BG,
                               variable=self.variable)
        slider.grid(row=1, column=0, columnspan=2, sticky='ew', padx=5, pady=5)

    def update_label(self, *args):
        new_value: str = str(round(self.variable.get(), 2))
        self.slide_value_indicator.configure(text=new_value)


class RotationPanel(SliderPanel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class ZoomPanel(SliderPanel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class InvertPanel(ctk.CTkFrame):
    def __init__(self, parent, flip_option):
        super().__init__(master=parent, fg_color=DARK_GREY)
        self.pack(fill='x', padx=5, pady=5)
        self.flip_option = flip_option
        self.set_layout()
        self.create_widgets()

    def set_layout(self):
        self.rowconfigure((0, 1), weight=1, uniform='a')
        self.columnconfigure(0, weight=1, uniform='b')

    def create_widgets(self):
        title_label = ctk.CTkLabel(self, text='Invert')
        title_label.grid(row=0, column=0, sticky='news', pady=5)

        flip_button = ctk.CTkSegmentedButton(self, values=FLIP_OPTIONS, variable=self.flip_option)
        flip_button.grid(row=1, column=0, sticky='news', pady=5)


class ColorSwitches(ctk.CTkFrame):
    def __init__(self, parent, grey_scale_var, invert_var):
        super().__init__(master=parent, fg_color=DARK_GREY)
        self.pack(padx=5, pady=5, fill='x')
        self.grey_scale_var = grey_scale_var
        self.invert_var = invert_var

        self.set_layout()
        self.create_widgets()

    def set_layout(self):
        self.rowconfigure(0, weight=1, uniform='a')
        self.columnconfigure((0, 1), weight=1, uniform='b')

    def create_widgets(self):
        black_or_white_switch = ctk.CTkSwitch(self, text='B/W', height=50, button_color=BLUE, fg_color=GREY,
                                              variable=self.grey_scale_var)
        black_or_white_switch.grid(row=0, column=0, padx=5)

        invert_color_switch = ctk.CTkSwitch(self, text='Invert', height=50, button_color=BLUE, fg_color=GREY,
                                            variable=self.invert_var)
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
