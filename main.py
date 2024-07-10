import customtkinter as ctk
from PIL import Image, ImageTk

from tabs import MyTabView
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
        self.image_selected.trace('w', self.initialize)
        self.bind('<<ApplyFilter>>', self.apply_filters)

        self.initialize()

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

    def initialize(self, *args) -> None:
        self.fully_initialed = False

        # Destroy all the widgets if they already exist.
        for widget in self.winfo_children():
            widget.destroy()

        self.create_variables()

        if self.image_selected.get():
            self.set_layout()

            self.image_frame = ImageFrame(self, self.imported_image.image_path, self.image_selected)
            self.tab_view = MyTabView(self,
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
                                      self.apply_filters,
                                      self.image_frame.get_original_image_path())
            self.fully_initialed = True
        else:
            self.imported_image = ImportImage(self, self.image_selected)

    def apply_filters(self, *args, export=False) -> Image:

        edited_img = self.image_frame.get_original_image_path() if export else self.image_frame.get_resize_img()

        if self.fully_initialed:
            # Apply each filter or transformation
            edited_img = self.get_rotation_panel().apply_rotation(edited_img)
            edited_img = self.get_zoom_panel().apply_zoom(edited_img, export=export)
            edited_img = self.get_invert_panel().apply_flip(edited_img)
            edited_img = self.get_color_switches().apply_black_and_white(edited_img)
            edited_img = self.get_color_switches().apply_color_inversion(edited_img)
            edited_img = self.get_brightness_panel().apply_brightness(edited_img)
            edited_img = self.get_vibrance_panel().apply_vibrance(edited_img)
            edited_img = self.get_contrast_panel().apply_contrast(edited_img)
            edited_img = self.get_blur_panel().apply_blur(edited_img)
            edited_img = self.get_effect_tab().apply_effect(edited_img)

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

    def get_rotation_panel(self):
        return self.tab_view.position_tab.rotation_menu

    def get_zoom_panel(self):
        return self.tab_view.position_tab.zoom_panel

    def get_invert_panel(self):
        return self.tab_view.position_tab.invert_panel

    def get_color_switches(self):
        return self.tab_view.color_tab.color_switches

    def get_brightness_panel(self):
        return self.tab_view.color_tab.brightness_panel

    def get_vibrance_panel(self):
        return self.tab_view.color_tab.vibrance_panel

    def get_contrast_panel(self):
        return self.tab_view.effects_tab.contrast_panel

    def get_blur_panel(self):
        return self.tab_view.effects_tab.blur_panel

    def get_effect_tab(self):
        return self.tab_view.effects_tab


if __name__ == '__main__':
    app = EditorApp()
    app.mainloop()
