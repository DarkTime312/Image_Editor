from tkinter import filedialog

import customtkinter as ctk
from PIL import Image, ImageTk, ImageOps, ImageEnhance, ImageFilter

from settings import *


class ImageFrame(ctk.CTkCanvas):
    def __init__(self, parent, image_path, image_selected, grey_scale_var,
                 invert_var, brightness_level, vibrance_level, blur_level,
                 contrast_level, effect_name, flip_option, rotation_degree,
                 zoom_level):
        super().__init__(master=parent, bg=BACKGROUND_COLOR, highlightthickness=0, borderwidth=0)
        self.grid(row=0, column=1, sticky='news', padx=10, pady=10)
        self.bind('<Configure>', self.resize_image)

        # Storing references
        self.image_path = image_path
        self.image_selected = image_selected
        self.grey_scale_var = grey_scale_var
        self.invert_var = invert_var
        self.brightness_level = brightness_level
        self.vibrance_level = vibrance_level
        self.blur_level = blur_level
        self.contrast_level = contrast_level
        self.effect_name = effect_name
        self.flip_option = flip_option
        self.rotation_degree = rotation_degree
        self.zoom_level = zoom_level

        # Create the Close image button
        CloseImageButton(self, image_selected)

        # bindings
        variables = (self.grey_scale_var, self.invert_var, self.brightness_level, self.vibrance_level,
                     self.blur_level, self.contrast_level, self.effect_name, self.flip_option,
                     self.rotation_degree, self.zoom_level)
        for variable in variables:
            variable.trace('w', self.apply_filters)

    def resize_image(self, event=None):
        """
        Resize the image based on the current window width and height maintaining
        the current aspect ratio.

        :param event: event object
        :return: None
        """

        window_width = event.width
        window_height = event.height

        image = self.image_path
        image_aspect_ratio = image.width / image.height
        window_aspect_ratio = window_width / window_height

        # Determine resize dimensions
        if image_aspect_ratio > window_aspect_ratio:
            # Fit to width
            self.width = window_width
            self.height = int(self.width / image_aspect_ratio)
        else:
            # Fit to height
            self.height = window_height
            self.width = int(self.height * image_aspect_ratio)

        self.resized_img = image.resize((self.width, self.height))
        self.x_center = window_width // 2
        self.y_center = window_height // 2
        self.apply_filters()

    def apply_filters(self, *args, export=False) -> Image:
        edited_img = self.image_path if export else self.resized_img

        # Apply each filter or transformation
        edited_img = self.apply_rotation(edited_img)
        edited_img = self.apply_zoom(edited_img, export=export)
        edited_img = self.apply_flip(edited_img)
        edited_img = self.apply_black_and_white(edited_img)
        edited_img = self.apply_color_inversion(edited_img)
        edited_img = self.apply_brightness(edited_img)
        edited_img = self.apply_vibrance(edited_img)
        edited_img = self.apply_contrast(edited_img)
        edited_img = self.apply_blur(edited_img)
        edited_img = self.apply_effect(edited_img)

        # If we're exporting an image
        if export:
            # resize the image only for display purposes
            # Use the last calculated size for the window
            display_img = edited_img.resize((self.width, self.height))
        else:
            # No need to resize because we already used a resized picture
            display_img = edited_img

        self.image_tk = ImageTk.PhotoImage(display_img)
        # Add the image on canvas
        self.create_image(self.x_center, self.y_center, anchor='center', image=self.image_tk)
        # Return the edited image, this only will be used when we export a picture
        return edited_img

    def apply_rotation(self, img):
        ration_degree: float = self.rotation_degree.get()
        rotation_is_active: bool = ration_degree != ROTATE_DEFAULT

        if rotation_is_active:
            # Rotate
            img = img.rotate(ration_degree, expand=True, resample=Image.BICUBIC)
        return img

    def apply_zoom(self, img, export):
        zoom_level: float = self.zoom_level.get()
        zoom_is_active: bool = zoom_level != ZOOM_DEFAULT

        if zoom_is_active:
            # Zoom by increasing the size of the image
            new_size = (int(img.width * zoom_level), int(img.height * zoom_level))
            img = img.resize(new_size, Image.LANCZOS)

            # If we're getting output image
            if export:
                # First store the original image dimensions
                old_width = self.image_path.width
                old_height = self.image_path.height

                left = (new_size[0] - old_width) // 2
                upper = (new_size[1] - old_height) // 2
                right = left + old_width
                lower = upper + old_height

                crop_region = (left, upper, right, lower)
                # Crop the image
                img = img.crop(crop_region)
        return img

    def apply_flip(self, img):
        flip_option: str = self.flip_option.get()
        flip_is_active: bool = flip_option != FLIP_OPTIONS[0]

        if flip_is_active:
            # set flip
            match flip_option:
                case 'X':
                    img = ImageOps.mirror(img)
                case 'Y':
                    img = ImageOps.flip(img)
                case 'Both':
                    img = ImageOps.mirror(img)
                    img = ImageOps.flip(img)
        return img

    def apply_black_and_white(self, img):
        black_and_white_is_active: bool = self.grey_scale_var.get()
        if black_and_white_is_active:
            img = img.convert("L")
        return img

    def apply_color_inversion(self, img):
        invert_color_is_active: bool = self.invert_var.get()
        if invert_color_is_active:
            # Convert the image to RGB mode if necessary
            if img.mode != 'RGB':
                img = img.convert('RGB')
            # Invert the colors of the image
            img = ImageOps.invert(img)

        return img

    def apply_brightness(self, img):
        brightness_level: float = self.brightness_level.get()
        brightness_is_active: bool = brightness_level != BRIGHTNESS_DEFAULT

        if brightness_is_active:
            # Set brightness
            enhancer = ImageEnhance.Brightness(img)
            img = enhancer.enhance(brightness_level)
        return img

    def apply_vibrance(self, img):
        vibrance_level: float = self.vibrance_level.get()
        vibrance_is_active: bool = vibrance_level != BRIGHTNESS_DEFAULT

        if vibrance_is_active:
            # set Vibrance
            enhancer = ImageEnhance.Color(img)
            img = enhancer.enhance(vibrance_level)

        return img

    def apply_contrast(self, img):
        contrast_level: float = self.contrast_level.get()
        contrast_is_active: bool = contrast_level != CONTRAST_DEFAULT
        if contrast_is_active:
            # Set contrast
            enhancer = ImageEnhance.Contrast(img)
            img = enhancer.enhance(contrast_level)

        return img

    def apply_blur(self, img):
        blur_level: float = self.blur_level.get()
        blur_is_active: bool = blur_level != BLUR_DEFAULT

        if blur_is_active:
            # Set Blur
            img = img.filter(ImageFilter.GaussianBlur(blur_level))

        return img

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


class ExportName(ctk.CTkFrame):
    def __init__(self, parent, output_img_name, output_img_extention, file_name):
        super().__init__(master=parent, fg_color=DARK_GREY)
        self.pack(padx=5, pady=5, fill='x')
        self.output_img_name = output_img_name
        self.file_name = file_name
        self.output_img_extention = output_img_extention

        self.output_img_name.trace('w', self.update_name)

        self.set_layout()
        self.create_widgets()

    def set_layout(self):
        self.rowconfigure((0, 1, 2), weight=1, uniform='a')
        self.columnconfigure((0, 1), weight=1, uniform='b')

    def create_widgets(self):
        file_name_entry = ctk.CTkEntry(self, width=180, textvariable=self.output_img_name)
        file_name_entry.grid(row=0, column=0, columnspan=2, padx=20, pady=5, sticky='ew')

        self.jpg_check_box = ctk.CTkCheckBox(self, text='jpg', variable=self.output_img_extention, onvalue=0,
                                             command=lambda: self.on_checkbox_change('jpg'))
        self.jpg_check_box.grid(row=1, column=0, padx=(40, 20))

        self.png_check_box = ctk.CTkCheckBox(self, text='png', variable=self.output_img_extention, onvalue=1,
                                             command=lambda: self.on_checkbox_change('png'))
        self.png_check_box.grid(row=1, column=1)

        image_name_label = ctk.CTkLabel(self, textvariable=self.file_name)
        image_name_label.grid(row=2, column=0, columnspan=2)

    def on_checkbox_change(self, selected_value):
        if selected_value == "jpg":
            self.jpg_check_box.select()
            self.png_check_box.deselect()
            self.update_name()
        elif selected_value == "png":
            self.jpg_check_box.deselect()
            self.png_check_box.select()
            self.update_name()

    def update_name(self, *args):
        user_entered_text = self.output_img_name.get()
        user_selected_ext = 'jpg' if self.output_img_extention.get() == 0 else 'png'
        if user_entered_text:
            self.file_name.set(f'{user_entered_text}.{user_selected_ext}')
        else:
            self.file_name.set('')


class ExportFolder(ctk.CTkFrame):
    def __init__(self, parent, save_location):
        super().__init__(master=parent, fg_color=DARK_GREY)
        self.pack(padx=5, pady=5, fill='x')
        self.save_location = save_location

        self.set_layout()
        self.create_widgets()

    def set_layout(self):
        self.rowconfigure((0, 1), weight=1)
        self.columnconfigure(0, weight=1, uniform='b')

    def create_widgets(self):
        select_folder_btn = ctk.CTkButton(self, text='Open Explorer', width=150, command=self.get_save_folder)
        select_folder_btn.grid(row=0, column=0, pady=5)

        self.save_folder_entry = ctk.CTkEntry(self, width=200, textvariable=self.save_location)
        self.save_folder_entry.grid(row=1, column=0, ipady=10, padx=5, pady=5, sticky='ew')

    def get_save_folder(self) -> None:
        """
        Prompts user to select a folder for saving the image.
        It then inserts the address into the entry box.

        :return: None
        """
        save_folder = filedialog.askdirectory(title='Select Folder')
        # If user selected a folder
        if save_folder:
            self.save_location.set(save_folder)


class ImportImage(ctk.CTkButton):
    def __init__(self, parent, image_selected):
        super().__init__(master=parent, text='Open image', width=150, command=self.select_image)
        self.image_selected = image_selected
        self.image_path = None
        self.place(relx=0.5, rely=0.5, anchor='center')

    def select_image(self):
        file_path = filedialog.askopenfilename(
            title="Open Image File",
            filetypes=[
                ("All Image Files",
                 "*.bmp;*.dib;*.eps;*.gif;*.icns;*.ico;*.im;*.jpeg;*.jpg;*.msp;*.pcx;*.png;*.ppm;*.pgm;*.pbm;*.sgi;*.spider;*.tga;*.tiff;*.tif;*.webp;*.xbm;*.xpm"),
                ("BMP Files", "*.bmp;*.dib"),
                ("EPS Files", "*.eps"),
                ("GIF Files", "*.gif"),
                ("ICNS Files", "*.icns"),
                ("ICO Files", "*.ico"),
                ("IM Files", "*.im"),
                ("JPEG Files", "*.jpeg;*.jpg"),
                ("MSP Files", "*.msp"),
                ("PCX Files", "*.pcx"),
                ("PNG Files", "*.png"),
                ("PPM Files", "*.ppm;*.pgm;*.pbm"),
                ("SGI Files", "*.sgi"),
                ("SPIDER Files", "*.spider"),
                ("TGA Files", "*.tga"),
                ("TIFF Files", "*.tiff;*.tif"),
                ("WEBP Files", "*.webp"),
                ("XBM Files", "*.xbm"),
                ("XPM Files", "*.xpm")
            ]
        )

        if file_path:
            self.image_path = Image.open(file_path)
            self.image_selected.set(True)


class CloseImageButton(ctk.CTkButton):
    """
    A button that will close the image and starts the app from beginning.
    """

    def __init__(self, parent, image_selected):
        super().__init__(master=parent,
                         text='X',
                         width=20,
                         height=20,
                         fg_color=BACKGROUND_COLOR,
                         hover_color=CLOSE_RED,
                         text_color=WHITE,
                         command=self.close_image)
        self.image_selected = image_selected
        self.place(relx=0.99, rely=0.01, anchor='ne')

    def close_image(self) -> None:
        """
        Changes the image_selected variable to False and that in itself
        will run the create_widgets function in the main.py
        :return: None
        """
        self.image_selected.set(False)
