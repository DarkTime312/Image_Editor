import customtkinter as ctk
from settings import *


class RotationPanel(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color=DARK_GREY)
        self.pack(fill='x', padx=5, pady=5)

        self.set_layout()
        self.create_widgets()

    def set_layout(self):
        self.rowconfigure((0, 1), weight=1, uniform='a')
        self.columnconfigure((0, 1), weight=1, uniform='b')

    def create_widgets(self):
        title_label = ctk.CTkLabel(self, text='Rotation')
        title_label.grid(row=0, column=0, sticky='w', padx=5, pady=5)

        rotation_degree_label = ctk.CTkLabel(self, text='0.0')
        rotation_degree_label.grid(row=0, column=1, sticky='e', padx=5, pady=5)

        rotation_slider = ctk.CTkSlider(self, from_=0, to=360)
        rotation_slider.grid(row=1, column=0, columnspan=2, sticky='ew', padx=5, pady=5)


class ZoomPanel(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color=DARK_GREY)
        self.pack(fill='x', padx=5, pady=5)

        self.set_layout()
        self.create_widgets()

    def set_layout(self):
        self.rowconfigure((0, 1), weight=1, uniform='a')
        self.columnconfigure((0, 1), weight=1, uniform='b')

    def create_widgets(self):
        title_label = ctk.CTkLabel(self, text='Zoom')
        title_label.grid(row=0, column=0, sticky='w', padx=5, pady=5)

        zoom_level_label = ctk.CTkLabel(self, text='0.0')
        zoom_level_label.grid(row=0, column=1, sticky='e', padx=5, pady=5)

        zoom_level_slider = ctk.CTkSlider(self, from_=0, to=200)
        zoom_level_slider.grid(row=1, column=0, columnspan=2, sticky='ew', padx=5, pady=5)


class InvertPanel(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color=DARK_GREY)
        self.pack(fill='x', padx=5, pady=5)

        self.set_layout()
        self.create_widgets()

    def set_layout(self):
        self.rowconfigure((0, 1), weight=1, uniform='a')
        self.columnconfigure((0, 1, 2, 3), weight=1, uniform='b')

    def create_widgets(self):
        title_label = ctk.CTkLabel(self, text='Invert')
        title_label.grid(row=0, column=1, columnspan=2)

        none_btn = ctk.CTkButton(self, text='None', fg_color=DARK_GREY, hover_color=GREY)
        none_btn.grid(row=1, column=0, padx=2, pady=5)

        x_btn = ctk.CTkButton(self, text='X', fg_color=DARK_GREY, hover_color=GREY)
        x_btn.grid(row=1, column=1, padx=2, pady=5)

        y_btn = ctk.CTkButton(self, text='Y', fg_color=DARK_GREY, hover_color=GREY)
        y_btn.grid(row=1, column=2, padx=2, pady=5)

        y_btn = ctk.CTkButton(self, text='Both', fg_color=DARK_GREY, hover_color=GREY)
        y_btn.grid(row=1, column=3, padx=2, pady=5)
