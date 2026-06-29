import customtkinter as ctk
from tkinter import filedialog


class LeftPanel:

    def __init__(self, parent, preview):

        self.preview = preview

        self.frame = ctk.CTkFrame(parent, width=300)
        self.frame.pack(
            side="left",
            fill="y",
            padx=10,
            pady=10
        )

        self.build_ui()

    def build_ui(self):

        title = ctk.CTkLabel(
            self.frame,
            text="Settings",
            font=("Segoe UI", 22, "bold")
        )
        title.pack(pady=20)

        browse_btn = ctk.CTkButton(
            self.frame,
            text="Browse Photo",
            command=self.browse_photo
        )
        browse_btn.pack(fill="x", padx=20, pady=10)

        paper_label = ctk.CTkLabel(
            self.frame,
            text="Paper Size"
        )
        paper_label.pack(anchor="w", padx=20)

        self.paper = ctk.CTkComboBox(
            self.frame,
            values=[
                "4×6",
                "5×7",
                "A4",
                "Letter"
            ]
        )
        self.paper.set("4×6")
        self.paper.pack(fill="x", padx=20, pady=5)

        photo_label = ctk.CTkLabel(
            self.frame,
            text="Photo Size"
        )
        photo_label.pack(anchor="w", padx=20)

        self.photo = ctk.CTkComboBox(
            self.frame,
            values=[
                "Stamp (2.5 × 3.5 cm)",
                "Passport (3.5 × 4.5 cm)",
                "Visa (35 × 45 mm)"
            ]
        )

        self.photo.set("Stamp (2.5 × 3.5 cm)")
        self.photo.pack(fill="x", padx=20, pady=5)

    def browse_photo(self):

        filename = filedialog.askopenfilename(
            title="Select Photo",
            filetypes=[
                ("Image Files", "*.jpg *.jpeg *.png *.bmp")
            ]
        )

        if filename:
            self.preview.load_image(filename)