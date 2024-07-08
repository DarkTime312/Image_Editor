import customtkinter as ctk
from settings import *
from panels import RotationPanel, ZoomPanel, InvertPanel


class MyTabView(ctk.CTkTabview):
    def __init__(self, master):
        super().__init__(master, fg_color=BACKGROUND_COLOR)
        self.grid(row=0, column=0, sticky='news')

        # create tabs
        position_frm = self.add("Position")
        color_frm = self.add("Color")
        effects_frm = self.add("Effects")
        export_frm = self.add("Export")

        PositionMenu(position_frm)
        ColorMenu(color_frm)
        EffectsMenu(effects_frm)
        ExportMenu(export_frm)


class PositionMenu(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent)
        self.pack(expand=True, fill='both', padx=5)

        RotationPanel(self)
        ZoomPanel(self)
        InvertPanel(self)

        revert_btn = ctk.CTkButton(self, text='Revert', width=150)
        revert_btn.pack(side='bottom', pady=15)


class ColorMenu(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color='blue')
        self.pack(expand=True, fill='both')


class EffectsMenu(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color='brown')
        self.pack(expand=True, fill='both')


class ExportMenu(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color='yellow')
        self.pack(expand=True, fill='both')
