import customtkinter as ctk


class Toolbar:

    def __init__(self, parent):

        self.frame = ctk.CTkFrame(parent, height=45)

        self.frame.pack(fill="x")

        self.preview = None

        self.btn_open = ctk.CTkButton(
            self.frame,
            text="Open"
        )

        self.btn_open.pack(side="left", padx=5, pady=5)

        self.btn_left = ctk.CTkButton(
            self.frame,
            text="Rotate Left",
            command=self.rotate_left
        )

        self.btn_left.pack(side="left", padx=5)

        self.btn_right = ctk.CTkButton(
            self.frame,
            text="Rotate Right",
            command=self.rotate_right
        )

        self.btn_right.pack(side="left", padx=5)

        self.btn_fit = ctk.CTkButton(
            self.frame,
            text="Fit",
            command=self.fit
        )

        self.btn_fit.pack(side="left", padx=5)

        self.btn_zoom_in = ctk.CTkButton(
            self.frame,
            text="Zoom +",
            command=self.zoom_in
        )

        self.btn_zoom_in.pack(side="left", padx=5)

        self.btn_zoom_out = ctk.CTkButton(
            self.frame,
            text="Zoom -",
            command=self.zoom_out
        )

        self.btn_zoom_out.pack(side="left", padx=5)

    def set_preview(self, preview):
        self.preview = preview

    def rotate_left(self):
        if self.preview:
            self.preview.rotate_left()

    def rotate_right(self):
        if self.preview:
            self.preview.rotate_right()

    def zoom_in(self):
        if self.preview:
            self.preview.zoom_in()

    def zoom_out(self):
        if self.preview:
            self.preview.zoom_out()

    def fit(self):
        if self.preview:
            self.preview.fit()