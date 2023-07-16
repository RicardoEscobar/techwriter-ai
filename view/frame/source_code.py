"""This module contains the SourceCodeFrame class.
It shows the source code for the application to work on."""

import tkinter as tk
from tkinter import ttk


class SourceCodeFrame(ttk.LabelFrame):
    """This tkinter frame shows the source code for the application to work on."""

    def __init__(self, parent, text: str = "Source Code"):
        """Initialize the SourceCodeFrame."""
        super().__init__(parent, text="Source Code")
        self.create_widgets()

    def create_widgets(self):
        """Create the widgets for the SourceCodeFrame."""
        self.source_code_text = tk.Text(self, wrap="word")
        self.source_code_scroll = ttk.Scrollbar(self, orient="vertical", command=self.source_code_text.yview)
        self.source_code_text.configure(yscrollcommand=self.source_code_scroll.set)

        self.source_code_text.grid(row=0, column=0, sticky="nsew")
        self.source_code_scroll.grid(row=0, column=0, sticky="nse")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)