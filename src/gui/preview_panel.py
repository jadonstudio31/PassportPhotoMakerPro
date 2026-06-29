import customtkinter as ctk
from PIL import Image, ImageTk


class PreviewPanel:

    def __init__(self, parent):

        self.frame = ctk.CTkFrame(parent)

        self.frame.pack(
            side="right",
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        self.label = ctk.CTkLabel(
            self.frame,
            text="No Image Loaded",
            font=("Segoe UI", 20)
        )

        self.label.pack(expand=True)

        self.original_image = None
        self.current_image = None
        self.tk_image = None

        self.zoom = 1.0
        self.rotation = 0

    def load_image(self, filename):

        self.original_image = Image.open(filename)

        self.zoom = 1.0
        self.rotation = 0

        self.update_preview()

    def update_preview(self):

        if self.original_image is None:
            return

        image = self.original_image.copy()

        if self.rotation != 0:
            image = image.rotate(
                self.rotation,
                expand=True
            )

        width = int(image.width * self.zoom)
        height = int(image.height * self.zoom)

        image = image.resize(
            (width, height),
            Image.LANCZOS
        )

        image.thumbnail((900, 650))

        self.tk_image = ImageTk.PhotoImage(image)

        self.label.configure(
            image=self.tk_image,
            text=""
        )

    def zoom_in(self):

        self.zoom *= 1.2

        self.update_preview()

    def zoom_out(self):

        self.zoom /= 1.2

        self.update_preview()

    def rotate_left(self):

        self.rotation -= 90

        self.update_preview()

    def rotate_right(self):

        self.rotation += 90

        self.update_preview()

    def fit(self):

        self.zoom = 1.0

        self.update_preview()