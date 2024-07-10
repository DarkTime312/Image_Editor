from tkinter import filedialog

import customtkinter as ctk
from PIL import Image

from settings import *


class ImageFrame(ctk.CTkCanvas):
    def __init__(self, parent, image_path, image_selected):
        super().__init__(master=parent, bg=BACKGROUND_COLOR, highlightthickness=0, borderwidth=0)
        self.grid(row=0, column=1, sticky='news', padx=10, pady=10)
        self.bind('<Configure>', self.resize_image)

        # Storing references
        self.image_path = image_path

        # Create the Close image button
        CloseImageButton(self, image_selected)

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
        self.event_generate('<<ApplyFilter>>')

    def get_win_size(self):
        return self.width, self.height

    def get_window_center(self):
        return self.x_center, self.y_center

    def get_resize_img(self):
        return self.resized_img

    def get_original_image_path(self):
        return self.image_path


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
