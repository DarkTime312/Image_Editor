import customtkinter as ctk
from PIL import Image, ImageTk, ImageOps, ImageEnhance, ImageFilter

from menu import MyTabView
from image_widgets import ImageFrame, ImportImage
from settings import *


class EditorApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        # Force dark mode
        ctk.set_appearance_mode('dark')
        # Window layout
        self.geometry('1000x600')
        self.title('Photo Editor')
        self.minsize(800, 500)

        # A flag that shows if an image is selected or not
        self.image_selected = ctk.BooleanVar(value=False)
        self.image_selected.trace('w', self.create_widgets)
        self.bind('<<ApplyFilter>>', self.apply_filters)

        self.create_widgets()

    def create_variables(self):
        # Image filter related variables
        self.rotation_degree = ctk.DoubleVar(value=ROTATE_DEFAULT)
        self.zoom_level = ctk.DoubleVar(value=ZOOM_DEFAULT)
        self.brightness_level = ctk.DoubleVar(value=BRIGHTNESS_DEFAULT)
        self.vibrance_level = ctk.DoubleVar(value=VIBRANCE_DEFAULT)
        self.blur_level = ctk.DoubleVar(value=BLUR_DEFAULT)
        self.contrast_level = ctk.DoubleVar(value=CONTRAST_DEFAULT)
        self.grey_scale_var = ctk.BooleanVar(value=GRAYSCALE_DEFAULT)
        self.invert_var = ctk.BooleanVar(value=INVERT_DEFAULT)
        self.effect_name = ctk.StringVar(value=EFFECT_OPTIONS[0])
        self.flip_option = ctk.StringVar(value=FLIP_OPTIONS[0])

        # bindings
        variables = (self.grey_scale_var, self.invert_var, self.brightness_level, self.vibrance_level,
                     self.blur_level, self.contrast_level, self.effect_name, self.flip_option,
                     self.rotation_degree, self.zoom_level)
        for variable in variables:
            variable.trace('w', self.apply_filters)

    def set_layout(self):
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1, uniform='a')
        self.columnconfigure(1, weight=3, uniform='a')

    def create_widgets(self, *args) -> None:
        # Destroy all the widgets if they already exist.
        for widget in self.winfo_children():
            widget.destroy()

        self.create_variables()

        if self.image_selected.get():
            self.set_layout()

            self.image_frame = ImageFrame(self, self.imported_image.image_path, self.image_selected)
            MyTabView(self,
                      self.brightness_level,
                      self.vibrance_level,
                      self.rotation_degree,
                      self.zoom_level,
                      self.blur_level,
                      self.contrast_level,
                      self.grey_scale_var,
                      self.invert_var,
                      self.effect_name,
                      self.flip_option,
                      self.apply_filters
                      )
        else:
            self.imported_image = ImportImage(self, self.image_selected)

    def apply_filters(self, *args, export=False) -> Image:

        edited_img = self.image_frame.get_original_image_path() if export else self.image_frame.get_resize_img()

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
            display_img = edited_img.resize(self.image_frame.get_win_size())
        else:
            # No need to resize because we already used a resized picture
            display_img = edited_img

        self.image_tk = ImageTk.PhotoImage(display_img)
        # Add the image on canvas
        self.image_frame.create_image(*self.image_frame.get_window_center(), anchor='center', image=self.image_tk)
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
                old_width = self.image_frame.get_original_image_path().width
                old_height = self.image_frame.get_original_image_path().height

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


if __name__ == '__main__':
    app = EditorApp()
    app.mainloop()
