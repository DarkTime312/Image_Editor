import customtkinter as ctk
from menu import MyTabView
from image_widgets import ImageFrame, ImportImage


class EditorApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        # Force dark mode
        ctk.set_appearance_mode('dark')
        # Window layout
        self.geometry('1000x600')
        self.title('Photo Editor')
        self.minsize(800, 500)

        # variables
        self.image_selected = ctk.BooleanVar(value=False)
        self.image_selected.trace('w', self.create_widgets)
        self.imported_image = ImportImage(self, self.image_selected)

    def set_layout(self):
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1, uniform='a')
        self.columnconfigure(1, weight=3, uniform='a')

    def create_widgets(self, *args):
        if self.image_selected.get():
            self.imported_image.place_forget()

            self.set_layout()
            MyTabView(self)
            ImageFrame(self, self.imported_image.image_path)


if __name__ == '__main__':
    app = EditorApp()
    app.mainloop()
