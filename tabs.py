from tkinter import messagebox

import customtkinter as ctk
from PIL import ImageFilter

from settings import *
from panels import RotationPanel, ZoomPanel, InvertPanel, ColorSwitches, BrightnessPanel, VibrancePanel, \
    BlurPanel, ContrastPanel, RevertButton, ExportName, ExportFolder


class MyTabView(ctk.CTkTabview):
    """
    A custom tab view for a photo editing application, containing tabs for position,
     color, effects, and export functionalities.

    This class extends the customtkinter CTkTabview and organizes the user interface into four main tabs:
    - Position: Controls for rotating, zooming, and flipping the image.
    - Color: Controls for adjusting brightness, vibrance, and applying color switches.
    - Effects: Controls for applying blur, contrast, and various image effects.
    - Export: Controls for exporting the edited image, including setting the file name and save location.
    """
    def __init__(self, master, variables_dict, apply_filters, original_img):
        super().__init__(master, fg_color=BACKGROUND_COLOR)
        self.grid(row=0, column=0, sticky='news')

        # Create tabs
        position_frm = self.add("Position")
        color_frm = self.add("Color")
        effects_frm = self.add("Effects")
        export_frm = self.add("Export")

        # Create frames for each tab
        self.position_tab = PositionTab(position_frm, variables_dict['position'], original_img)
        self.color_tab = ColorTab(color_frm, variables_dict['color'])
        self.effects_tab = EffectsTab(effects_frm, variables_dict['effects'])
        ExportTab(export_frm, apply_filters)


class PositionTab(ctk.CTkFrame):
    """
    A custom frame for managing image position adjustments in a photo editing application.

    This class extends the customtkinter CTkFrame and provides controls for rotating, zooming, and flipping an image.
    It also includes a revert button to reset these adjustments to their default values.
    """
    def __init__(self, parent, position_dict, original_img):
        super().__init__(master=parent)
        self.pack(expand=True, fill='both', padx=5)

        self.rotation_menu = RotationPanel(parent=self, text='Rotation', max_value=360, variable=position_dict['rotation'][0])
        self.zoom_panel = ZoomPanel(parent=self, text='Zoom', max_value=2, variable=position_dict['zoom'][0], org_img=original_img)
        self.invert_panel = InvertPanel(self, position_dict['flip'][0])

        RevertButton(self, position_dict)


class ColorTab(ctk.CTkFrame):
    """
    A custom frame for managing color adjustments in a photo editing application.

    This class extends the customtkinter CTkFrame and provides controls for adjusting brightness, vibrance,
    grayscale, and inversion of an image. It also includes a revert button to reset these adjustments to their default values.
    """
    def __init__(self, parent, color_dict):
        super().__init__(master=parent)
        self.pack(expand=True, fill='both')

        self.color_switches = ColorSwitches(self, color_dict['grey_scale'][0], color_dict['invert'][0])
        self.brightness_panel = BrightnessPanel(parent=self, text='Brightness', max_value=5, variable=color_dict['brightness'][0])
        self.vibrance_panel = VibrancePanel(parent=self, text='Vibrance', max_value=5, variable=color_dict['vibrance'][0])

        RevertButton(self, color_dict)


class EffectsTab(ctk.CTkFrame):
    """
    A custom frame for managing image effects in a photo editing application.

    This class extends the customtkinter CTkFrame and provides controls for applying blur, contrast, and various image effects.
    It also includes a revert button to reset these adjustments to their default values.
    """
    def __init__(self, parent, effects_dict):
        super().__init__(master=parent)
        self.pack(expand=True, fill='both')
        self.effect_name = effects_dict['effect'][0]

        effect_options = ctk.CTkOptionMenu(self,
                                           values=EFFECT_OPTIONS,
                                           fg_color=DARK_GREY,
                                           dropdown_fg_color=DROPDOWN_MENU_COLOR,
                                           button_color=DROPDOWN_MAIN_COLOR,
                                           button_hover_color=DROPDOWN_HOVER_COLOR,
                                           variable=self.effect_name,
                                           )
        effect_options.pack(fill='x', padx=5, pady=5)

        self.blur_panel = BlurPanel(parent=self, text='Blur', max_value=30, variable=effects_dict['blur'][0])

        self.contrast_panel = ContrastPanel(parent=self, text='Contrast', max_value=10, variable=effects_dict['contrast'][0])

        RevertButton(self, effects_dict)

    def apply_effect(self, img):
        """
        Applies the selected effect to the given image.

        Parameters:
            img (PIL.Image.Image): The image to which the effect will be applied.

        Returns:
            PIL.Image.Image: The image with the applied effect.
        """
        # Get the selected effect name from the effect_name variable
        effect_name: str = self.effect_name.get()
        # Check if the selected effect is not the default option
        effect_is_active: bool = effect_name != EFFECT_OPTIONS[0]

        if effect_is_active:
            # Apply the selected effect based on the effect_name
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
                    # Raise an exception if the effect name is unknown
                    raise Exception('Unknown filter!')

            # Apply the selected filter to the image
            img = img.filter(filter_name)

        # Return the image with the applied effect
        return img


class ExportTab(ctk.CTkFrame):
    """
    A custom frame for managing the export of edited images in a photo editing application.

    This class extends the customtkinter CTkFrame and provides controls for setting the output file name,
    save location, and exporting the image.
    """
    def __init__(self, parent, apply_filters):
        super().__init__(master=parent)
        self.pack(expand=True, fill='both')
        # A function to apply filters to the image before saving.
        self.apply_filters = apply_filters

        # Variables for output file
        self.save_location = ctk.StringVar()
        self.output_img_name = ctk.StringVar()  # Name of the file
        self.output_img_extension = ctk.StringVar(value='.jpg')  # Extension
        self.file_name = ctk.StringVar()  # Full file name (name + extension)

        self.create_widgets()

    def create_widgets(self):
        """
        Creates and packs the widgets for setting the output file name and save location.
        """

        ExportName(self, self.output_img_name, self.output_img_extension, self.file_name)
        ExportFolder(self, self.save_location)

        save_btn = ctk.CTkButton(self, text='Save', width=150, command=self.save_file)
        save_btn.pack(side='bottom', pady=15)

    def save_file(self):
        """
        Saves the edited image to the specified location with the specified file name and extension.
        """
        # Get the full file name and save location
        file_name = self.file_name.get()
        folder_name = self.save_location.get()

        # Check if both file name and folder name are provided
        if file_name and folder_name:
            # Construct the final file path
            final_address = f'{folder_name}/{file_name}'
            # Apply filters to the image before saving
            image = self.apply_filters(export=True)
            # Convert RGBA to RGB if saving as JPG
            if 'jpg' in file_name and image.mode == 'RGBA':
                image = image.convert('RGB')
            # Save the image to the final address
            image.save(final_address)
            # Opening a messagebox indicating to the user that the image has been saved
            messagebox.showinfo(title='File saved', message=f'{file_name} saved!')
