import customtkinter as ctk

from tkinter import filedialog
from PIL import Image
from PIL import ImageTk


class MainWindow:

    def __init__(self, root):

        self.root = root

        self.image = None
        self.photo = None

        self.build_ui()

    def build_ui(self):

        self.left = ctk.CTkFrame(self.root, width=300)
        self.left.pack(side="left", fill="y", padx=10, pady=10)

        self.right = ctk.CTkFrame(self.root)
        self.right.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        title = ctk.CTkLabel(
            self.left,
            text="Passport Photo Sheet Maker Pro",
            font=("Segoe UI", 22, "bold")
        )

        title.pack(pady=20)

        browse = ctk.CTkButton(
            self.left,
            text="Browse Photo",
            command=self.open_image
        )

        browse.pack(fill="x", padx=20, pady=10)

        paper = ctk.CTkLabel(self.left, text="Paper Size")
        paper.pack(anchor="w", padx=20)

        self.paper = ctk.CTkComboBox(
            self.left,
            values=["4×6", "5×7", "A4", "Letter"]
        )

        self.paper.set("4×6")
        self.paper.pack(fill="x", padx=20, pady=5)

        photo = ctk.CTkLabel(self.left, text="Photo Size")
        photo.pack(anchor="w", padx=20)

        self.photo_size = ctk.CTkComboBox(
            self.left,
            values=[
                "Stamp (2.5 × 3.5 cm)",
                "Passport (3.5 × 4.5 cm)",
                "Visa (35 × 45 mm)"
            ]
        )

        self.photo_size.set("Stamp (2.5 × 3.5 cm)")
        self.photo_size.pack(fill="x", padx=20, pady=5)

        ctk.CTkButton(
            self.left,
            text="Generate Sheet"
        ).pack(fill="x", padx=20, pady=30)

        self.preview = ctk.CTkLabel(
            self.right,
            text="No Image Selected"
        )

        self.preview.pack(expand=True)

        self.status = ctk.CTkLabel(
            self.root,
            text="Ready",
            anchor="w"
        )

        self.status.pack(fill="x", side="bottom")

    def open_image(self):

        filename = filedialog.askopenfilename(
            filetypes=[
                ("Images", "*.jpg *.jpeg *.png *.bmp")
            ]
        )

        if not filename:
            return

        self.image = Image.open(filename)

        preview = self.image.copy()

        preview.thumbnail((850, 650))

        self.photo = ImageTk.PhotoImage(preview)

        self.preview.configure(image=self.photo, text="")

        self.status.configure(text=filename)