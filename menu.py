import customtkinter as ctk

from settings import *
from panels import RotationPanel, ZoomPanel, InvertPanel, ColorSwitches, BrightnessPanel, VibrancePanel, \
    BlurPanel, ContrastPanel
from image_widgets import ExportName, ExportFolder


class MyTabView(ctk.CTkTabview):
    def __init__(self, master, brightness_level, vibrance_level, rotation_degree, zoom_level, blur_level,
                 contrast_level, grey_scale_var, invert_var, effect_name, flip_option, apply_filters):
        super().__init__(master, fg_color=BACKGROUND_COLOR)
        self.grid(row=0, column=0, sticky='news')

        # create tabs
        position_frm = self.add("Position")
        color_frm = self.add("Color")
        effects_frm = self.add("Effects")
        export_frm = self.add("Export")

        PositionMenu(position_frm, rotation_degree, zoom_level, flip_option)
        ColorMenu(color_frm, brightness_level, vibrance_level, grey_scale_var, invert_var)
        EffectsMenu(effects_frm, blur_level, contrast_level, effect_name)
        ExportMenu(export_frm, apply_filters)


class PositionMenu(ctk.CTkFrame):
    def __init__(self, parent, rotation_degree, zoom_level, flip_option):
        super().__init__(master=parent)
        self.pack(expand=True, fill='both', padx=5)

        RotationPanel(parent=self, text='Rotation', max_value=360, variable=rotation_degree)
        ZoomPanel(parent=self, text='Zoom', max_value=2, variable=zoom_level)
        InvertPanel(self, flip_option)

        RevertButton(self, ((rotation_degree, ROTATE_DEFAULT),
                            (zoom_level, ZOOM_DEFAULT),
                            (flip_option, FLIP_OPTIONS[0])
                            ))


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
    def __init__(self, parent, blur_level, contrast_level, effect_name):
        super().__init__(master=parent)
        self.pack(expand=True, fill='both')

        effect_options = ctk.CTkOptionMenu(self,
                                           values=EFFECT_OPTIONS,
                                           fg_color=DARK_GREY,
                                           dropdown_fg_color=DROPDOWN_MENU_COLOR,
                                           button_color=DROPDOWN_MAIN_COLOR,
                                           button_hover_color=DROPDOWN_HOVER_COLOR,
                                           variable=effect_name)
        effect_options.pack(fill='x', padx=5, pady=5)

        BlurPanel(parent=self, text='Blur', max_value=30, variable=blur_level)
        ContrastPanel(parent=self, text='Contrast', max_value=10, variable=contrast_level)

        RevertButton(self, ((effect_name, EFFECT_OPTIONS[0]),
                            (blur_level, BLUR_DEFAULT),
                            (contrast_level, CONTRAST_DEFAULT)
                            ))


class ExportMenu(ctk.CTkFrame):
    def __init__(self, parent, apply_filters):
        super().__init__(master=parent)
        self.pack(expand=True, fill='both')
        self.apply_filters = apply_filters

        # Output file name variables
        self.save_location = ctk.StringVar()
        self.output_img_name = ctk.StringVar()  # Name of the file
        self.output_img_extension = ctk.StringVar(value='.jpg')  # extension
        self.file_name = ctk.StringVar()  # Full file name (name + ext)

        self.create_widgets()

    def create_widgets(self):
        ExportName(self, self.output_img_name, self.output_img_extension, self.file_name)
        ExportFolder(self, self.save_location)

        save_btn = ctk.CTkButton(self, text='Save', width=150, command=self.save_file)
        save_btn.pack(side='bottom', pady=15)

    def save_file(self):
        file_name = self.file_name.get()
        folder_name = self.save_location.get()
        if file_name and folder_name:
            final_address = f'{folder_name}/{file_name}'
            image = self.apply_filters(export=True)
            if 'jpg' in file_name and image.mode == 'RGBA':
                image = image.convert('RGB')
            image.save(final_address)


class RevertButton(ctk.CTkButton):
    def __init__(self, parent, defaults):
        super().__init__(master=parent, text='Revert', width=150, command=lambda: self.revert(defaults))
        self.pack(side='bottom', pady=15)

    def revert(self, defaults: tuple[tuple]):
        for variable, value in defaults:
            variable.set(value)
