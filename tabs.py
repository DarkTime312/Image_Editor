import customtkinter as ctk
from PIL import ImageFilter

from settings import *
from panels import RotationPanel, ZoomPanel, InvertPanel, ColorSwitches, BrightnessPanel, VibrancePanel, \
    BlurPanel, ContrastPanel, RevertButton, ExportName, ExportFolder


class MyTabView(ctk.CTkTabview):
    def __init__(self, master, brightness_level, vibrance_level, rotation_degree, zoom_level, blur_level,
                 contrast_level, grey_scale_var, invert_var, effect_name, flip_option, apply_filters, original_img):
        super().__init__(master, fg_color=BACKGROUND_COLOR)
        self.grid(row=0, column=0, sticky='news')

        # create tabs
        position_frm = self.add("Position")
        color_frm = self.add("Color")
        effects_frm = self.add("Effects")
        export_frm = self.add("Export")

        self.position_tab = PositionTab(position_frm, rotation_degree, zoom_level, flip_option, original_img)
        self.color_tab = ColorTab(color_frm, brightness_level, vibrance_level, grey_scale_var, invert_var)
        self.effects_tab = EffectsTab(effects_frm, blur_level, contrast_level, effect_name)
        ExportTab(export_frm, apply_filters)


class PositionTab(ctk.CTkFrame):
    def __init__(self, parent, rotation_degree, zoom_level, flip_option, original_img):
        super().__init__(master=parent)
        self.pack(expand=True, fill='both', padx=5)

        self.rotation_menu = RotationPanel(parent=self, text='Rotation', max_value=360, variable=rotation_degree)
        self.zoom_panel = ZoomPanel(parent=self, text='Zoom', max_value=2, variable=zoom_level, org_img=original_img)
        self.invert_panel = InvertPanel(self, flip_option)

        RevertButton(self, ((rotation_degree, ROTATE_DEFAULT),
                            (zoom_level, ZOOM_DEFAULT),
                            (flip_option, FLIP_OPTIONS[0])
                            ))


class ColorTab(ctk.CTkFrame):
    def __init__(self, parent, brightness_level, vibrance_level, grey_scale_var, invert_var):
        super().__init__(master=parent)
        self.pack(expand=True, fill='both')

        self.color_switches = ColorSwitches(self, grey_scale_var, invert_var)
        self.brightness_panel = BrightnessPanel(parent=self, text='Brightness', max_value=5, variable=brightness_level)
        self.vibrance_panel = VibrancePanel(parent=self, text='Vibrance', max_value=5, variable=vibrance_level)

        RevertButton(self, ((grey_scale_var, GRAYSCALE_DEFAULT),
                            (invert_var, INVERT_DEFAULT),
                            (brightness_level, BRIGHTNESS_DEFAULT),
                            (vibrance_level, VIBRANCE_DEFAULT)
                            ))


class EffectsTab(ctk.CTkFrame):
    def __init__(self, parent, blur_level, contrast_level, effect_name):
        super().__init__(master=parent)
        self.pack(expand=True, fill='both')
        self.effect_name = effect_name

        effect_options = ctk.CTkOptionMenu(self,
                                           values=EFFECT_OPTIONS,
                                           fg_color=DARK_GREY,
                                           dropdown_fg_color=DROPDOWN_MENU_COLOR,
                                           button_color=DROPDOWN_MAIN_COLOR,
                                           button_hover_color=DROPDOWN_HOVER_COLOR,
                                           variable=effect_name)
        effect_options.pack(fill='x', padx=5, pady=5)

        self.blur_panel = BlurPanel(parent=self, text='Blur', max_value=30, variable=blur_level)
        self.contrast_panel = ContrastPanel(parent=self, text='Contrast', max_value=10, variable=contrast_level)

        RevertButton(self, ((effect_name, EFFECT_OPTIONS[0]),
                            (blur_level, BLUR_DEFAULT),
                            (contrast_level, CONTRAST_DEFAULT)
                            ))

    def apply_effect(self, img):
        effect_name: str = self.effect_name.get()
        effect_is_active: bool = effect_name != EFFECT_OPTIONS[0]

        if effect_is_active:
            # Apply effect
            match effect_name:
                case 'Emboss':
                    filter_name = ImageFilter.EMBOSS
                case 'Find edges':
                    filter_name = ImageFilter.FIND_EDGES
                case 'Contour':
                    filter_name = ImageFilter.CONTOUR
                case 'Edge enhance':
                    filter_name = ImageFilter.EDGE_ENHANCE
                case _:
                    raise Exception('Unknown filter!')

            img = img.filter(filter_name)

        return img


class ExportTab(ctk.CTkFrame):
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
