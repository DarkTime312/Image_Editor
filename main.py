import customtkinter as ctk
from PIL import Image, ImageTk

from image_widgets import ImageFrame, ImportImage
from settings import *
from tabs import MyTabView


class EditorApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        # Class attributes
        self.variables_dict = None
        self.image_tk = None
        self.tab_view = None
        self.image_frame = None
        self.original_img_path = None
        self.imported_image = None

        # Force dark mode
        ctk.set_appearance_mode('dark')

        # Window setup
        self.geometry('1000x600')
        self.title('Photo Editor')
        self.minsize(800, 500)

        # A flag that shows if user has selected an image or not
        self.image_selected = ctk.BooleanVar(value=False)
        # Initialize the app each time the value of the flag changes
        self.image_selected.trace('w', self.initialize)

        # A custom event
        self.bind('<<ApplyFilter>>', self.apply_filters)

        # Initialize the app for the first time
        self.initialize()

    def initialize(self, *args) -> None:
        """
        Initializes the application interface based on whether an image has been selected or not.

        This function is triggered whenever the `image_selected` variable changes. It first destroys
        all existing widgets to reset the interface. If an image has been selected, it sets up the
        necessary variables, layout, and widgets for editing the image. If no image is selected, it
        displays a button to import an image.

        :param args: [Not used] Only present to work with trace mechanism.
        :return: None
        """

        # Destroy all the widgets if they already exist.
        for widget in self.winfo_children():
            widget.destroy()

        # If user has selected an image
        if self.image_selected.get():
            # Create necessary variables for image editing
            self.create_variables()
            # Set the layout for the widgets
            self.set_layout()
            # Get the path of the original image
            self.original_img_path = self.imported_image.get_original_image_path()

            # Create an ImageFrame widget to display and edit the image
            self.image_frame = ImageFrame(self, self.original_img_path, self.image_selected)

            # Create a MyTabView widget to hold the editing controls
            self.tab_view = MyTabView(self,
                                      self.variables_dict,
                                      self.apply_filters,
                                      self.original_img_path)

        # If the user hasn't selected any image yet
        else:
            # Create the import image button to allow the user to select an image
            self.imported_image = ImportImage(self, self.image_selected)

    def create_variables(self) -> None:
        """
        Creates the necessary tkinter variables and passes them default
        values from settings module.

        It also binds the variables to the apply_filters function.

        :return: None
        """
        self.variables_dict = {
            'position': {
                'rotation': (ctk.DoubleVar(), ROTATE_DEFAULT),
                'zoom': (ctk.DoubleVar(), ZOOM_DEFAULT),
                'flip': (ctk.StringVar(), FLIP_OPTIONS[0])
            },
            'color': {
                'grey_scale': (ctk.BooleanVar(), GRAYSCALE_DEFAULT),
                'invert': (ctk.BooleanVar(), INVERT_DEFAULT),
                'brightness': (ctk.DoubleVar(), BRIGHTNESS_DEFAULT),
                'vibrance': (ctk.DoubleVar(), VIBRANCE_DEFAULT)

            },
            'effects': {
                'effect': (ctk.StringVar(), EFFECT_OPTIONS[0]),
                'blur': (ctk.DoubleVar(), BLUR_DEFAULT),
                'contrast': (ctk.DoubleVar(), CONTRAST_DEFAULT)
            }
        }

        # Set the default value and tracing for each variable
        for panels in self.variables_dict.values():
            for variable, default_value in panels.values():
                variable.set(default_value)
                variable.trace('w', self.apply_filters)

    def set_layout(self) -> None:
        """
        Sets the grid layout for the widgets.
        It only runs when user already selected an image.

        :return: None
        """
        self.rowconfigure(0, weight=1)

        self.columnconfigure(0, weight=1, uniform='a')
        self.columnconfigure(1, weight=3, uniform='a')

    def apply_filters(self, *args, export=False) -> Image:
        """
        Applies a series of image filters and transformations to the currently loaded image.

        This function is triggered whenever any of the image editing variables change, or when
        the custom '<<ApplyFilter>>' event is generated. It processes the image through various
        filters and transformations such as rotation, zoom, flip, color adjustments, brightness,
        vibrance, contrast, blur, and effects.

        :param args: [Not used] Only present to work with trace mechanism.
        :param export: Boolean flag indicating whether the function is being called for exporting the image.
                       If True, the image is processed at its original size. If False, the image is processed
                       at a resized version suitable for display.
        :return: The edited PIL Image object.
        """
        # Get the original image path if exporting, otherwise get the resized image for display
        edited_img = self.original_img_path if export else self.image_frame.get_resized_img()

        # Apply rotation to the image
        edited_img = self.get_rotation_panel().apply_rotation(edited_img)
        # Apply zoom to the image
        edited_img = self.get_zoom_panel().apply_zoom(edited_img, export=export)
        # Apply flip (invert) transformations to the image
        edited_img = self.get_invert_panel().apply_flip(edited_img)
        # Apply grayscale transformation to the image
        edited_img = self.get_color_switches().apply_black_and_white(edited_img)
        # Apply color inversion to the image
        edited_img = self.get_color_switches().apply_color_inversion(edited_img)
        # Apply brightness adjustment to the image
        edited_img = self.get_brightness_panel().apply_brightness(edited_img)
        # Apply vibrance adjustment to the image
        edited_img = self.get_vibrance_panel().apply_vibrance(edited_img)
        # Apply contrast adjustment to the image
        edited_img = self.get_contrast_panel().apply_contrast(edited_img)
        # Apply blur effect to the image
        edited_img = self.get_blur_panel().apply_blur(edited_img)
        # Apply additional effects to the image
        edited_img = self.get_effect_tab().apply_effect(edited_img)

        # If exporting the image, resize it for display purposes
        if export:
            # Resize the image to fit the display window size
            display_img = edited_img.resize(self.image_frame.get_win_size())
        else:
            # Use the already resized image for display
            display_img = edited_img

        # Convert the edited image to a format suitable for displaying in Tkinter
        self.image_tk = ImageTk.PhotoImage(display_img)
        # Display the image on the canvas
        self.image_frame.create_image(*self.image_frame.get_window_center(), anchor='center', image=self.image_tk)

        # Return the edited image, useful when exporting the image
        return edited_img

    def get_rotation_panel(self):
        """
        Retrieves the rotation panel from the position tab.
        """
        return self.tab_view.position_tab.rotation_menu

    def get_zoom_panel(self):
        """
        Retrieves the zoom panel from the position tab.
        """
        return self.tab_view.position_tab.zoom_panel

    def get_invert_panel(self):
        """
        Retrieves the invert (flip) panel from the position tab.
        """
        return self.tab_view.position_tab.invert_panel

    def get_color_switches(self):
        """
        Retrieves the color switches panel from the color tab.
        """
        return self.tab_view.color_tab.color_switches

    def get_brightness_panel(self):
        """
        Retrieves the brightness panel from the color tab.
        """
        return self.tab_view.color_tab.brightness_panel

    def get_vibrance_panel(self):
        """
        Retrieves the vibrance panel from the color tab.
        """
        return self.tab_view.color_tab.vibrance_panel

    def get_contrast_panel(self):
        """
        Retrieves the contrast panel from the effects tab.
        """
        return self.tab_view.effects_tab.contrast_panel

    def get_blur_panel(self):
        """
        Retrieves the blur panel from the effects tab.
        """
        return self.tab_view.effects_tab.blur_panel

    def get_effect_tab(self):
        """
        Retrieves the effect tab from the effects tab.
        """
        return self.tab_view.effects_tab


if __name__ == '__main__':
    app = EditorApp()
    app.mainloop()
