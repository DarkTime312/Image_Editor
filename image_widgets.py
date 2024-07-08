import customtkinter as ctk
from settings import *
from tkinter import filedialog
from PIL import Image, ImageTk


class ImageFrame(ctk.CTkCanvas):
    def __init__(self, parent, image_path):
        super().__init__(master=parent, bg=BACKGROUND_COLOR, highlightthickness=0, borderwidth=0)
        self.grid(row=0, column=1, sticky='news', padx=10, pady=10)
        self.bind('<Configure>', self.resize_image)
        self.image_path = image_path

    def resize_image(self, event):
        """
        Resize the image based on the current window width and height maintaining
        the current aspect ratio.

        :param event: event object
        :return: None
        """
        window_width = event.width
        window_height = event.height
        # print(window_width, window_height)
        image = Image.open(self.image_path)
        image_aspect_ratio = image.width / image.height
        window_aspect_ratio = window_width / window_height

        # Determine resize dimensions
        if image_aspect_ratio > window_aspect_ratio:
            # Fit to width
            width = window_width
            height = int(width / image_aspect_ratio)
        else:
            # Fit to height
            height = window_height
            width = int(height * image_aspect_ratio)

        resized_img = image.resize((width, height))
        self.image_tk = ImageTk.PhotoImage(resized_img)

        self.create_image(window_width // 2, window_height // 2, anchor='center', image=self.image_tk)


class ExportName(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color=DARK_GREY)
        self.pack(padx=5, pady=5, fill='x')

        self.set_layout()
        self.create_widgets()

    def set_layout(self):
        self.rowconfigure((0, 1, 2), weight=1, uniform='a')
        self.columnconfigure((0, 1), weight=1, uniform='b')

    def create_widgets(self):
        file_name_entry = ctk.CTkEntry(self, width=180)
        file_name_entry.grid(row=0, column=0, columnspan=2, padx=20, pady=5, sticky='ew')

        jpg_check_box = ctk.CTkCheckBox(self, text='jpg')
        jpg_check_box.grid(row=1, column=0, padx=(40, 20))

        png_check_box = ctk.CTkCheckBox(self, text='png')
        png_check_box.grid(row=1, column=1)

        image_name_label = ctk.CTkLabel(self, text='file.png')
        image_name_label.grid(row=2, column=0, columnspan=2)


class ExportFolder(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color=DARK_GREY)
        self.pack(padx=5, pady=5, fill='x')

        self.set_layout()
        self.create_widgets()

    def set_layout(self):
        self.rowconfigure((0, 1), weight=1)
        self.columnconfigure(0, weight=1, uniform='b')

    def create_widgets(self):
        select_folder_btn = ctk.CTkButton(self, text='Open Explorer', width=150, command=self.get_save_folder)
        select_folder_btn.grid(row=0, column=0, pady=5)

        self.save_folder_entry = ctk.CTkEntry(self, width=200)
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
            # First clear the entry box
            self.save_folder_entry.delete(0, 'end')
            # Then put the address into entry box
            self.save_folder_entry.insert(0, save_folder)


class ImportImage(ctk.CTkButton):
    def __init__(self, parent, image_selected):
        super().__init__(master=parent, text='Open image', width=150, command=self.select_image)
        self.image_selected = image_selected
        self.image_path = None
        self.place(relx=0.5, rely=0.5, anchor='center')

    def select_image(self):
        img_file = filedialog.askopenfilename(title='Open')
        if img_file:
            self.image_path = img_file
            self.image_selected.set(True)
