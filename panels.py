from tkinter import filedialog

import customtkinter as ctk

from settings import *
from PIL import Image, ImageOps, ImageEnhance, ImageFilter


class SliderPanel(ctk.CTkFrame):
    """
    A panel containing a slider and a label to adjust and display a value.

    This class extends the customtkinter CTkFrame and provides a slider to adjust a value,
    and a label to display the current value of the slider.
    """
    def __init__(self, parent, text, max_value, variable, from_=0):
        super().__init__(master=parent, fg_color=DARK_GREY)
        self.text = text
        self.max_value = max_value
        self.variable = variable
        self.from_ = from_
        self.pack(fill='x', padx=5, pady=5)

        self.set_layout()
        self.create_widgets()
        self.variable.trace('w', self.update_label)
        self.update_label()

    def set_layout(self):
        """
        Configures the grid layout for the panel.
        """
        self.rowconfigure((0, 1), weight=1, uniform='a')
        self.columnconfigure((0, 1), weight=1, uniform='b')

    def create_widgets(self):
        """
        Creates and places the widgets (slider and labels) within the panel.
        """
        # Create and place the title label
        title_label = ctk.CTkLabel(self, text=self.text)
        title_label.grid(row=0, column=0, sticky='w', padx=5, pady=5)

        # Create and place the label to display the slider value
        self.slide_value_indicator = ctk.CTkLabel(self)
        self.slide_value_indicator.grid(row=0, column=1, sticky='e', padx=5, pady=5)

        # Create and place the slider
        slider = ctk.CTkSlider(self,
                               from_=self.from_,
                               to=self.max_value,
                               fg_color=SLIDER_BG,
                               variable=self.variable)
        slider.grid(row=1, column=0, columnspan=2, sticky='ew', padx=5, pady=5)

    def update_label(self, *args):
        """
        Updates the label to display the current value of the slider.

        :param args: Additional arguments (not used).
        """

        new_value: str = str(round(self.variable.get(), 2))
        self.slide_value_indicator.configure(text=new_value)


class RotationPanel(SliderPanel):
    """
    A panel for adjusting the rotation of an image.

    This class extends the SliderPanel and provides functionality to apply rotation to an image.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def apply_rotation(self, img):
        """
        Applies the rotation to the given image based on the slider value.

        :param img: The image to be rotated.
        :return: The rotated image.
        """

        ration_degree: float = self.variable.get()
        rotation_is_active: bool = ration_degree != ROTATE_DEFAULT

        if rotation_is_active:
            # Rotate the image
            img = img.rotate(ration_degree, expand=True, resample=Image.BICUBIC)
        return img


class ZoomPanel(SliderPanel):
    """
    A panel for adjusting the zoom level of an image.

    This class extends the SliderPanel and provides functionality to apply zoom to an image.
    """
    def __init__(self, org_img, **kwargs):
        """
        Initializes the ZoomPanel with the given parameters and sets up the layout and widgets.

        :param org_img: The original image before zooming.
        :param kwargs: Additional keyword arguments for the SliderPanel.
        """

        super().__init__(from_=0.5, **kwargs)
        self.original_img = org_img

    def apply_zoom(self, img, export):
        """
        Applies the zoom to the given image based on the slider value.

        :param img: The image to be zoomed.
        :param export: A boolean indicating whether the image is being exported.
        :return: The zoomed image.
        """

        zoom_level: float = self.variable.get()
        zoom_is_active: bool = zoom_level != ZOOM_DEFAULT

        if zoom_is_active:
            # Zoom by increasing the size of the image
            new_size = (int(img.width * zoom_level), int(img.height * zoom_level))
            img = img.resize(new_size, Image.LANCZOS)

            # If we're getting output image
            if export:
                # First store the original image dimensions
                old_width = self.original_img.width
                old_height = self.original_img.height

                left = (new_size[0] - old_width) // 2
                upper = (new_size[1] - old_height) // 2
                right = left + old_width
                lower = upper + old_height

                crop_region = (left, upper, right, lower)
                # Crop the image
                img = img.crop(crop_region)
        return img


class InvertPanel(ctk.CTkFrame):
    """
    A panel for inverting the image.

    This class extends the customtkinter CTkFrame and provides functionality to flip the image.
    """
    def __init__(self, parent, flip_option):
        super().__init__(master=parent, fg_color=DARK_GREY)
        self.pack(fill='x', padx=5, pady=5)
        self.flip_option = flip_option
        self.set_layout()
        self.create_widgets()

    def set_layout(self):
        """
        Configures the grid layout for the panel.
        """

        self.rowconfigure((0, 1), weight=1, uniform='a')
        self.columnconfigure(0, weight=1, uniform='b')

    def create_widgets(self):
        """
        Creates and places the widgets (flip options) within the panel.
        """
        # Create and place the title label
        title_label = ctk.CTkLabel(self, text='Invert')
        title_label.grid(row=0, column=0, sticky='news', pady=5)

        # Create and place the flip option button
        flip_button = ctk.CTkSegmentedButton(self, values=FLIP_OPTIONS, variable=self.flip_option)
        flip_button.grid(row=1, column=0, sticky='news', pady=5)

    def apply_flip(self, img):
        """
        Applies the flip to the given image based on the selected flip option.

        :param img: The image to be flipped.
        :return: The flipped image.
        """

        flip_option: str = self.flip_option.get()
        flip_is_active: bool = flip_option != FLIP_OPTIONS[0]

        if flip_is_active:
            # Apply the flip based on the selected option
            match flip_option:
                case 'X':
                    img = ImageOps.mirror(img)
                case 'Y':
                    img = ImageOps.flip(img)
                case 'Both':
                    img = ImageOps.mirror(img)
                    img = ImageOps.flip(img)
        return img


class ColorSwitches(ctk.CTkFrame):
    """
    A panel containing switches for black-and-white and color inversion.

    This class extends the customtkinter CTkFrame and provides functionality to apply black-and-white
    and color inversion effects to an image.
    """
    def __init__(self, parent, grey_scale_var, invert_var):
        """
        Initializes the ColorSwitches panel with the given parameters and sets up the layout and widgets.

        :param parent: The parent widget.
        :param grey_scale_var: The variable to bind to the black-and-white switch.
        :param invert_var: The variable to bind to the color inversion switch.
        """

        super().__init__(master=parent, fg_color=DARK_GREY)
        self.pack(padx=5, pady=5, fill='x')
        self.grey_scale_var = grey_scale_var
        self.invert_var = invert_var

        self.set_layout()
        self.create_widgets()

    def set_layout(self):
        """
        Configures the grid layout for the panel.
        """
        self.rowconfigure(0, weight=1, uniform='a')
        self.columnconfigure((0, 1), weight=1, uniform='b')

    def create_widgets(self):
        """
        Creates and places the widgets (switches) within the panel.
        """

        # Create and place the black-and-white switch
        black_or_white_switch = ctk.CTkSwitch(self, text='B/W', height=50, button_color=BLUE, fg_color=GREY,
                                              variable=self.grey_scale_var)
        black_or_white_switch.grid(row=0, column=0, padx=5)

        # Create and place the color inversion switch
        invert_color_switch = ctk.CTkSwitch(self, text='Invert', height=50, button_color=BLUE, fg_color=GREY,
                                            variable=self.invert_var)
        invert_color_switch.grid(row=0, column=1, padx=5)

    def apply_black_and_white(self, img):
        """
        Applies the black-and-white effect to the given image based on the switch value.

        :param img: The image to be converted to black-and-white.
        :return: The black-and-white image.
        """

        black_and_white_is_active: bool = self.grey_scale_var.get()
        if black_and_white_is_active:
            img = img.convert("L")
        return img

    def apply_color_inversion(self, img):
        """
        Applies the color inversion effect to the given image based on the switch value.

        :param img: The image to be color-inverted.
        :return: The color-inverted image.
        """

        invert_color_is_active: bool = self.invert_var.get()
        if invert_color_is_active:
            # Convert the image to RGB mode if necessary
            if img.mode != 'RGB':
                img = img.convert('RGB')
            # Invert the colors of the image
            img = ImageOps.invert(img)

        return img


class BrightnessPanel(SliderPanel):
    """
    A panel for adjusting the brightness of an image.

    This class extends the SliderPanel and provides functionality to apply brightness adjustments to an image.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def apply_brightness(self, img):
        """
        Applies the brightness adjustment to the given image based on the slider value.

        :param img: The image to be adjusted for brightness.
        :return: The brightness-adjusted image.
        """

        brightness_level: float = self.variable.get()
        brightness_is_active: bool = brightness_level != BRIGHTNESS_DEFAULT

        if brightness_is_active:
            # Set brightness
            enhancer = ImageEnhance.Brightness(img)
            img = enhancer.enhance(brightness_level)
        return img


class VibrancePanel(SliderPanel):
    """
    A panel for adjusting the vibrance of an image.

    This class extends the SliderPanel and provides functionality to apply vibrance adjustments to an image.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def apply_vibrance(self, img):
        """
        Applies the vibrance adjustment to the given image based on the slider value.

        :param img: The image to be adjusted for vibrance.
        :return: The vibrance-adjusted image.
        """

        vibrance_level: float = self.variable.get()
        vibrance_is_active: bool = vibrance_level != BRIGHTNESS_DEFAULT

        if vibrance_is_active:
            # set Vibrance
            enhancer = ImageEnhance.Color(img)
            img = enhancer.enhance(vibrance_level)

        return img


class BlurPanel(SliderPanel):
    """
    A panel for adjusting the blur level of an image.

    This class extends the SliderPanel and provides functionality to apply blur effects to an image.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def apply_blur(self, img):
        """
        Applies the blur effect to the given image based on the slider value.

        :param img: The image to be blurred.
        :return: The blurred image.
        """

        blur_level: float = self.variable.get()
        blur_is_active: bool = blur_level != BLUR_DEFAULT

        if blur_is_active:
            # Set Blur
            img = img.filter(ImageFilter.GaussianBlur(blur_level))

        return img


class ContrastPanel(SliderPanel):
    """
    A panel for adjusting the contrast of an image.

    This class extends the SliderPanel and provides functionality to apply contrast adjustments to an image.
    """

    def __init__(self, **kwargs):
        super().__init__(from_=0.5, **kwargs)

    def apply_contrast(self, img):
        """
        Applies the contrast adjustment to the given image based on the slider value.

        :param img: The image to be adjusted for contrast.
        :return: The contrast-adjusted image.
        """

        contrast_level: float = self.variable.get()
        contrast_is_active: bool = contrast_level != CONTRAST_DEFAULT
        if contrast_is_active:
            # Set contrast
            enhancer = ImageEnhance.Contrast(img)
            img = enhancer.enhance(contrast_level)

        return img


class ExportName(ctk.CTkFrame):
    """
    A panel for setting the export file name and extension.

    This class extends the customtkinter CTkFrame and provides functionality to set the export file name
    and extension for the image.
    """
    def __init__(self, parent, output_img_name, output_img_extension, file_name):
        """
        Initializes the ExportName panel with the given parameters and sets up the layout and widgets.

        :param parent: The parent widget.
        :param output_img_name: The variable to bind to the file name entry.
        :param output_img_extension: The variable to bind to the file extension checkboxes.
        :param file_name: The variable to display the full file name.
        """

        super().__init__(master=parent, fg_color=DARK_GREY)
        self.pack(padx=5, pady=5, fill='x')

        self.output_img_name = output_img_name
        self.file_name = file_name
        self.output_img_extension = output_img_extension

        # Trace changes to the output_img_name variable to update the file name
        self.output_img_name.trace('w', self.update_name)

        self.set_layout()
        self.create_widgets()

    def set_layout(self):
        """
        Configures the grid layout for the panel.
        """

        self.rowconfigure((0, 1, 2), weight=1, uniform='a')
        self.columnconfigure((0, 1), weight=1, uniform='b')

    def create_widgets(self):
        """
        Creates and places the widgets (entry, checkboxes, and label) within the panel.
        """
        # Create and place the entry widget for the file name
        file_name_entry = ctk.CTkEntry(self, width=180, textvariable=self.output_img_name)
        file_name_entry.grid(row=0, column=0, columnspan=2, padx=20, pady=5, sticky='ew')

        # Create and place the checkbox for the .jpg extension
        self.jpg_check_box = ctk.CTkCheckBox(self, text='jpg', variable=self.output_img_extension, onvalue='.jpg',
                                             command=lambda: self.on_checkbox_change('.jpg'))
        self.jpg_check_box.grid(row=1, column=0, padx=(40, 20))

        # Create and place the checkbox for the .png extension
        self.png_check_box = ctk.CTkCheckBox(self, text='png', variable=self.output_img_extension, onvalue='.png',
                                             command=lambda: self.on_checkbox_change('.png'))
        self.png_check_box.grid(row=1, column=1)

        # Create and place the label to display the full file name
        image_name_label = ctk.CTkLabel(self, textvariable=self.file_name)
        image_name_label.grid(row=2, column=0, columnspan=2)

    def on_checkbox_change(self, selected_value):
        """
        Handles the checkbox change event to ensure only one extension is selected at a time.

        :param selected_value: The selected extension value ('.jpg' or '.png').
        """

        if selected_value == ".jpg":
            self.png_check_box.deselect()
            self.jpg_check_box.select()

        elif selected_value == ".png":
            self.jpg_check_box.deselect()
            self.png_check_box.select()
        self.update_name()

    def update_name(self, *args):
        """
        Updates the full file name based on the user-entered name and selected extension.

        :param args: Additional arguments (not used).
        """

        user_entered_text = self.output_img_name.get()
        user_selected_ext = self.output_img_extension.get()
        # If user has entered a name
        if user_entered_text:
            self.file_name.set(f'{user_entered_text}{user_selected_ext}')
        else:
            self.file_name.set('')


class ExportFolder(ctk.CTkFrame):
    """
    A panel for selecting the export folder.

    This class extends the customtkinter CTkFrame and provides functionality to select a folder
    where the image will be saved.
    """
    def __init__(self, parent, save_location):
        """
        Initializes the ExportFolder panel with the given parameters and sets up the layout and widgets.

        :param parent: The parent widget.
        :param save_location: The variable to bind to the folder path entry.
        """

        super().__init__(master=parent, fg_color=DARK_GREY)
        self.pack(padx=5, pady=5, fill='x')
        self.save_location = save_location

        self.set_layout()
        self.create_widgets()

    def set_layout(self):
        """
        Configures the grid layout for the panel.
        """

        self.rowconfigure((0, 1), weight=1)
        self.columnconfigure(0, weight=1, uniform='b')

    def create_widgets(self):
        """
        Creates and places the widgets (button and entry) within the panel.
        """
        # Create and place the button to open the folder explorer
        select_folder_btn = ctk.CTkButton(self, text='Open Explorer', width=150, command=self.get_save_folder)
        select_folder_btn.grid(row=0, column=0, pady=5)

        # Create and place the entry widget to display the selected folder path
        self.save_folder_entry = ctk.CTkEntry(self, width=200, textvariable=self.save_location)
        self.save_folder_entry.grid(row=1, column=0, ipady=10, padx=5, pady=5, sticky='ew')

    def get_save_folder(self) -> None:
        """
        Prompts the user to select a folder for saving the image.
        It then inserts the address into the entry box.

        :return: None
        """
        save_folder = filedialog.askdirectory(title='Select Folder')
        # If user selected a folder
        if save_folder:
            self.save_location.set(save_folder)


def revert(defaults: tuple[tuple]) -> None:
    """
    Reverts a set of variables to their default values.

    This function iterates over a tuple of tuples, where each inner tuple contains a variable and its default value.
    It sets each variable to its corresponding default value.

    :param defaults: A tuple of tuples, where each inner tuple contains a variable and its default value.
    """

    for variable, value in defaults:
        variable.set(value)


class RevertButton(ctk.CTkButton):
    """
    A button that reverts variables to their default values when clicked.

    This class extends the customtkinter CTkButton and provides a button that, when clicked,
    reverts a set of variables to their default values.
    """
    def __init__(self, parent, defaults):
        super().__init__(master=parent, text='Revert', width=150, command=lambda: revert(defaults))
        self.pack(side='bottom', pady=15)
