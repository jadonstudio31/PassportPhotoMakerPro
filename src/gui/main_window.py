import customtkinter as ctk

from gui.toolbar import Toolbar
from gui.left_panel import LeftPanel
from gui.preview_panel import PreviewPanel
from gui.status_bar import StatusBar


class MainWindow:

    def __init__(self, root):

        self.root = root

        self.build_ui()

    def build_ui(self):

        # Toolbar
        self.toolbar = Toolbar(self.root)

        # Main Container
        self.main = ctk.CTkFrame(self.root)
        self.main.pack(
            fill="both",
            expand=True
        )

        # Preview Panel
        self.preview = PreviewPanel(self.main)

        # Left Panel
        self.left = LeftPanel(
            self.main,
            self.preview
        )

        # Status Bar
        self.status = StatusBar(self.root)