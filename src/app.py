import customtkinter as ctk
from gui import MainWindow

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class PassportPhotoMakerApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Passport Photo Sheet Maker Pro")
        self.geometry("1300x800")
        self.minsize(1200, 700)

        MainWindow(self)