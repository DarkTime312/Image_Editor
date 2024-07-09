import customtkinter as ctk
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
        self.image_selected = ctk.BooleanVar(value=False)
        self.image_selected.trace('w', self.create_widgets)

        self.create_widgets()

    def create_variables(self):
        # variables
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
        self.output_img_name = ctk.StringVar()
        self.output_img_extention = ctk.IntVar(value=0)
        self.file_name = ctk.StringVar()

    def set_layout(self):
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1, uniform='a')
        self.columnconfigure(1, weight=3, uniform='a')

    def create_widgets(self, *args):
        for widget in self.winfo_children():
            widget.destroy()

        self.create_variables()

        if self.image_selected.get():
            self.set_layout()
            self.image_frame = ImageFrame(self, self.imported_image.image_path, self.image_selected,
                                          self.grey_scale_var,
                                          self.invert_var, self.brightness_level, self.vibrance_level, self.blur_level,
                                          self.contrast_level, self.effect_name, self.flip_option, self.rotation_degree,
                                          self.zoom_level)
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
                      self.output_img_name,
                      self.output_img_extention,
                      self.file_name,
                      self.image_frame
                      )
        else:
            self.imported_image = ImportImage(self, self.image_selected)


if __name__ == '__main__':
    app = EditorApp()
    app.mainloop()
