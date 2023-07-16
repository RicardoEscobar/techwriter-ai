"""This frame contains widgets for the user to input text for the: system, user, and assistant
roles."""
import tkinter as tk
from tkinter import ttk

from controller.input import InputController

class InputFrame(ttk.LabelFrame):
    """This frame contains widgets for the user to input text for the: system, user, and assistant"""

    def __init__(self, parent, text: str = "System"):
        """Initialize the InputFrame."""
        super().__init__(parent, text=text)
        self.controller = InputController(label_text=text)        

        # Change input frame's border color to yellow for visibility
        self.configure(borderwidth=5, relief="groove")
        self.create_widgets()

    def create_widgets(self):
        """Create the widgets for the InputFrame."""

        # Add an entry field to the frame
        self.system_text = tk.Text(self, height=3, wrap="word")
        # Add a scrollbar to the entry field
        self.system_scroll = ttk.Scrollbar(self, orient="vertical", command=self.system_text.yview)
        self.system_text.configure(yscrollcommand=self.system_scroll.set)

        # Add a button to the frame
        self.prompt_button = ttk.Button(self, text="Prompt", command=self.controller)

        # Add the widgets to the frame
        self.system_text.grid(row=0, column=0, sticky="ew")
        self.system_scroll.grid(row=0, column=0, sticky="nse")
        self.prompt_button.grid(row=0, column=1, sticky="new")

        # make the self.system_text field expand to fill the frame
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)