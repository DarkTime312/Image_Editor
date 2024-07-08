import customtkinter as ctk
from menu import MyTabView
from image_widgets import ImageFrame


class EditorApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        # Force dark mode
        ctk.set_appearance_mode('dark')
        # Window layout
        self.geometry('1000x600')
        self.title('Photo Editor')
        self.minsize(800, 500)

        self.set_layout()

        # MenuFrame(self)
        MyTabView(self)
        ImageFrame(self)

    def set_layout(self):
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1, uniform='a')
        self.columnconfigure(1, weight=3, uniform='a')


if __name__ == '__main__':
    app = EditorApp()
    app.mainloop()
