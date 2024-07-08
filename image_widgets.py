import customtkinter as ctk
from settings import *


class ImageFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color='blue')
        self.grid(row=0, column=1, sticky='news')


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
        file_name_entry.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

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
        select_folder_btn = ctk.CTkButton(self, text='Open Explorer', width=150)
        select_folder_btn.grid(row=0, column=0, pady=5)

        save_folder_entry = ctk.CTkEntry(self, width=200)
        save_folder_entry.grid(row=1, column=0, ipady=10, pady=5)
