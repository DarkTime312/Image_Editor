import customtkinter as ctk
from settings import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageOps, ImageEnhance, ImageFilter


class ImageFrame(ctk.CTkCanvas):
    def __init__(self, parent, image_path, image_selected, grey_scale_var,
                 invert_var, brightness_level, vibrance_level, blur_level,
                 contrast_level, effect_name, flip_option, rotation_degree,
                 zoom_level):
        super().__init__(master=parent, bg=BACKGROUND_COLOR, highlightthickness=0, borderwidth=0)
        self.grid(row=0, column=1, sticky='news', padx=10, pady=10)
        self.bind('<Configure>', self.resize_image)
        self.image_path = image_path
        self.image_selected = image_selected
        self.grey_scale_var = grey_scale_var
        self.invert_var = invert_var
        self.brightness_level = brightness_level
        self.vibrance_level = vibrance_level
        self.blur_level = blur_level
        self.contrast_level = contrast_level
        self.effect_name = effect_name
        self.flip_option = flip_option
        self.rotation_degree = rotation_degree
        self.zoom_level = zoom_level

        CloseImageButton(self, image_selected)

        # bindings
        self.grey_scale_var.trace('w', self.update_picture)
        self.invert_var.trace('w', self.update_picture)
        self.brightness_level.trace('w', self.update_picture)
        self.vibrance_level.trace('w', self.update_picture)
        self.blur_level.trace('w', self.update_picture)
        self.contrast_level.trace('w', self.update_picture)
        self.effect_name.trace('w', self.update_picture)
        self.flip_option.trace('w', self.update_picture)
        self.rotation_degree.trace('w', self.update_picture)
        self.zoom_level.trace('w', self.update_picture)

    def resize_image(self, event=None):
        """
        Resize the image based on the current window width and height maintaining
        the current aspect ratio.

        :param event: event object
        :return: None
        """

        window_width = event.width
        window_height = event.height
        # print(window_width, window_height)
        image = self.image_path
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

        self.resized_img = image.resize((width, height))
        self.x_center = window_width // 2
        self.y_center = window_height // 2
        self.update_picture()

    def update_picture(self, *args):
        edited_img = self.resized_img
        # Rotate
        ration_degree = self.rotation_degree.get()
        edited_img = edited_img.rotate(ration_degree, expand=True)
        # Zoom
        zoom_level = self.zoom_level.get()
        new_size = (int(edited_img.width * zoom_level), int(edited_img.height * zoom_level))
        print(new_size)
        edited_img = edited_img.resize(new_size, Image.LANCZOS)

        # set flip
        flip_option = self.flip_option.get()
        if flip_option != 'None':
            match flip_option:
                case 'X':
                    edited_img = ImageOps.mirror(edited_img)
                case 'Y':
                    edited_img = ImageOps.flip(edited_img)
                case 'Both':
                    edited_img = ImageOps.mirror(edited_img)
                    edited_img = ImageOps.flip(edited_img)

        if self.grey_scale_var.get():
            edited_img = edited_img.convert("L")
        if self.invert_var.get():
            # Convert the image to RGB mode if necessary
            if edited_img.mode != 'RGB':
                edited_img = edited_img.convert('RGB')
            # Invert the colors of the image
            edited_img = ImageOps.invert(edited_img)

        # Set brightness
        brightness_level = self.brightness_level.get()
        enhancer = ImageEnhance.Brightness(edited_img)
        edited_img = enhancer.enhance(brightness_level)
        # set Vibrance
        vibrance_level = self.vibrance_level.get()
        enhancer = ImageEnhance.Color(edited_img)
        edited_img = enhancer.enhance(vibrance_level)
        # Set Blur
        blur_level = self.blur_level.get()
        edited_img = edited_img.filter(ImageFilter.GaussianBlur(blur_level))
        # Set contrast
        contrast_level = self.contrast_level.get()
        enhancer = ImageEnhance.Contrast(edited_img)
        edited_img = enhancer.enhance(contrast_level)
        # Apply effect
        effect_name = self.effect_name.get()
        if effect_name != 'None':
            match effect_name:
                case 'Emboss':
                    filter_name = ImageFilter.EMBOSS
                case 'Find edges':
                    filter_name = ImageFilter.FIND_EDGES
                case 'Contour':
                    filter_name = ImageFilter.CONTOUR
                case 'Edge enhance':
                    filter_name = ImageFilter.EDGE_ENHANCE
                case _:
                    return

            edited_img = edited_img.filter(filter_name)
        self.final_image = edited_img
        self.image_tk = ImageTk.PhotoImage(edited_img)
        self.create_image(self.x_center, self.y_center, anchor='center', image=self.image_tk)

    def get_image(self):
        return self.final_image
        # location = "C:/Users/rozes/OneDrive/Desktop/test.png"
        # self.final_image.save(location)
        # print('saved?')



class ExportName(ctk.CTkFrame):
    def __init__(self, parent, output_img_name, output_img_extention, file_name):
        super().__init__(master=parent, fg_color=DARK_GREY)
        self.pack(padx=5, pady=5, fill='x')
        self.output_img_name = output_img_name
        self.file_name = file_name
        self.output_img_extention = output_img_extention

        self.output_img_name.trace('w', self.update_name)

        self.set_layout()
        self.create_widgets()

    def set_layout(self):
        self.rowconfigure((0, 1, 2), weight=1, uniform='a')
        self.columnconfigure((0, 1), weight=1, uniform='b')

    def create_widgets(self):
        file_name_entry = ctk.CTkEntry(self, width=180, textvariable=self.output_img_name)
        file_name_entry.grid(row=0, column=0, columnspan=2, padx=20, pady=5, sticky='ew')

        self.jpg_check_box = ctk.CTkCheckBox(self, text='jpg', variable=self.output_img_extention, onvalue=0,
                                             command=lambda: self.on_checkbox_change('jpg'))
        self.jpg_check_box.grid(row=1, column=0, padx=(40, 20))

        self.png_check_box = ctk.CTkCheckBox(self, text='png', variable=self.output_img_extention, onvalue=1,
                                             command=lambda: self.on_checkbox_change('png'))
        self.png_check_box.grid(row=1, column=1)

        image_name_label = ctk.CTkLabel(self, textvariable=self.file_name)
        image_name_label.grid(row=2, column=0, columnspan=2)

    def on_checkbox_change(self, selected_value):
        if selected_value == "jpg":
            self.jpg_check_box.select()
            self.png_check_box.deselect()
            self.update_name()
        elif selected_value == "png":
            self.jpg_check_box.deselect()
            self.png_check_box.select()
            self.update_name()

    def update_name(self, *args):
        user_entered_text = self.output_img_name.get()
        user_selected_ext = 'jpg' if self.output_img_extention.get() == 0 else 'png'
        print(user_selected_ext)
        if user_entered_text:
            self.file_name.set(f'{user_entered_text}.{user_selected_ext}')
        else:
            self.file_name.set('')


class ExportFolder(ctk.CTkFrame):
    def __init__(self, parent, save_location):
        super().__init__(master=parent, fg_color=DARK_GREY)
        self.pack(padx=5, pady=5, fill='x')
        self.save_location = save_location

        self.set_layout()
        self.create_widgets()

    def set_layout(self):
        self.rowconfigure((0, 1), weight=1)
        self.columnconfigure(0, weight=1, uniform='b')

    def create_widgets(self):
        select_folder_btn = ctk.CTkButton(self, text='Open Explorer', width=150, command=self.get_save_folder)
        select_folder_btn.grid(row=0, column=0, pady=5)

        self.save_folder_entry = ctk.CTkEntry(self, width=200, textvariable=self.save_location)
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
            self.save_location.set(save_folder)


class ImportImage(ctk.CTkButton):
    def __init__(self, parent, image_selected):
        super().__init__(master=parent, text='Open image', width=150, command=self.select_image)
        self.image_selected = image_selected
        self.image_path = None
        self.place(relx=0.5, rely=0.5, anchor='center')

    def select_image(self):
        img_file = filedialog.askopenfilename(title='Open')
        if img_file:
            self.image_path = Image.open(img_file)
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
