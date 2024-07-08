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

        self.rotation_degree = ctk.DoubleVar(value=0.0)
        self.zoom_level = ctk.DoubleVar(value=0.0)
        self.brightness_level = ctk.DoubleVar(value=1.0)
        self.vibrance_level = ctk.DoubleVar(value=1.0)

        self.blur_level = ctk.DoubleVar(value=0.0)
        self.contrast_level = ctk.IntVar(value=0)

        self.create_widgets()

    def set_layout(self):
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1, uniform='a')
        self.columnconfigure(1, weight=3, uniform='a')

    def create_widgets(self, *args):
        for widget in self.winfo_children():
            widget.destroy()

        if self.image_selected.get():
            # self.imported_image.place_forget()

            self.set_layout()
            MyTabView(self,
                      self.brightness_level,
                      self.vibrance_level,
                      self.rotation_degree,
                      self.zoom_level,
                      self.blur_level,
                      self.contrast_level)
            ImageFrame(self, self.imported_image.image_path, self.image_selected)
        else:
            self.imported_image = ImportImage(self, self.image_selected)


if __name__ == '__main__':
    app = EditorApp()
    app.mainloop()
