import customtkinter as ctk


class ImageFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color='blue')
        self.grid(row=0, column=1, sticky='news')
