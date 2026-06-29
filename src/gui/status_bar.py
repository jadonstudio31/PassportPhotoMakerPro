import customtkinter as ctk


class StatusBar:

    def __init__(self, parent):

        self.label = ctk.CTkLabel(
            parent,
            text="Ready",
            anchor="w"
        )

        self.label.pack(fill="x", side="bottom")

    def set(self, text):
        self.label.configure(text=text)