from tkinter import filedialog

import customtkinter as ctk
from PIL import Image

from settings import *


class ImageFrame(ctk.CTkCanvas):
    """
    A custom canvas for displaying and resizing an image in a photo editing application.

    This class extends the customtkinter CTkCanvas and provides functionality to resize the image
    based on the current window dimensions while maintaining the aspect ratio.
    """

    def __init__(self, parent, original_img_path, image_selected):
        super().__init__(master=parent, bg=BACKGROUND_COLOR, highlightthickness=0, borderwidth=0)
        self.grid(row=0, column=1, sticky='news', padx=10, pady=10)
        self.bind('<Configure>', self.resize_image)

        # Storing references
        self.original_img_path = original_img_path

        # Class Attributes
        self.y_center = None
        self.x_center = None
        self.resized_img = None
        self.width = None
        self.height = None

        # Create the Close image button
        CloseImageButton(self, image_selected)

    def resize_image(self, event=None):
        """
        Resize the image based on the current window width and height maintaining
        the current aspect ratio.

        :param event: event object
        :return: None
        """
        # Get the current window dimensions from the event object
        window_width: int = event.width
        window_height: int = event.height

        # Calculate the aspect ratio of the original image
        image_aspect_ratio: float = self.original_img_path.width / self.original_img_path.height
        # Calculate the aspect ratio of the window
        window_aspect_ratio: float = window_width / window_height

        # Determine the dimensions to resize the image while maintaining its aspect ratio
        if image_aspect_ratio > window_aspect_ratio:
            # If the image is wider than the window, fit the image to the window's width
            self.width: int = window_width
            # Calculate the height to maintain the aspect ratio
            self.height: int = int(self.width / image_aspect_ratio)
        else:
            # If the image is taller than the window, fit the image to the window's height
            self.height: int = window_height
            # Calculate the width to maintain the aspect ratio
            self.width: int = int(self.height * image_aspect_ratio)

        # Resize the original image to the calculated dimensions
        self.resized_img: Image = self.original_img_path.resize((self.width, self.height))

        # Calculate the center coordinates of the window
        self.x_center: int = window_width // 2
        self.y_center: int = window_height // 2

        # Trigger the '<<ApplyFilter>>' event after a short delay to apply any filters to the resized image
        # Had to apply a little delay because of a bug that would cause <Configure> event to get triggered early
        self.after(5, lambda: self.event_generate('<<ApplyFilter>>'))

    def get_win_size(self) -> tuple[int, int]:
        """
        Returns the current width and height of the resized image.

        :return: tuple (width, height)
        """
        return self.width, self.height

    def get_window_center(self) -> tuple[int, int]:
        """
        Returns the current center coordinates of the resized image.

        :return: tuple (x_center, y_center)
        """
        return self.x_center, self.y_center

    def get_resized_img(self) -> Image:
        """
        Returns the resized image.

        :return: PIL.Image.Image
        """
        return self.resized_img


class ImportImage(ctk.CTkButton):
    """
    A custom button for importing images in a photo editing application.

    This class extends the customtkinter CTkButton and provides functionality to open a file dialog
    for selecting an image file from the file system. Once an image is selected, it updates the
    `image_selected` variable and stores the image path.
    """

    def __init__(self, parent, image_selected):
        super().__init__(master=parent, text='Open image', width=150, command=self.select_image)
        self.image_selected = image_selected
        self.image_path = None

        # Place the button in the center of the parent widget
        self.place(relx=0.5, rely=0.5, anchor='center')

    def select_image(self) -> None:
        """
        Prompts the user to select an image file from the file system.

        If the user selects an image, this function will update the image_path attribute with the selected image
        and set the image_selected variable to True, which in turn will trigger the initialize function to run again.

        :return: None
        """
        # Open a file dialog to select an image file
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
        # If a file was selected
        if file_path:
            # Open the selected image file and store the reference in image_path
            self.image_path = Image.open(file_path)
            # Set the image_selected variable to True to indicate an image has been selected
            self.image_selected.set(True)

    def get_original_image_path(self) -> Image:
        """
        Returns the selected image as a PIL Image object.

        This function will be used to get access to the image throughout the app.

        :return: The selected image saved as an Image object.
        """
        return self.image_path


class CloseImageButton(ctk.CTkButton):
    """
    A button that will close the image and restart the app from the beginning.

    This class extends the customtkinter CTkButton and provides functionality to close the currently
    selected image by setting the image_selected variable to False. This action triggers the app to
    restart from the beginning.
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
        # Place the button in the top-right corner of the parent widget
        self.place(relx=0.99, rely=0.01, anchor='ne')

    def close_image(self) -> None:
        """
        Sets the image_selected variable to False, triggering the app to restart.

        This function changes the image_selected variable to False, which in turn will run the
        initialize function in the main.py file to restart the app from the beginning.

        :return: None
        """
        self.image_selected.set(False)
