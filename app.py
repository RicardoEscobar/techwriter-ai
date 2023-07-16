"""This is a placeholder file for the app.py file."""
from tkinter import Tk
from tkinter import ttk

from view.frame.main import MainFrame


class App(Tk):
    """This is the main application class."""

    def __init__(self):
        """Initialize the App."""
        super().__init__()
        self.create_widgets()

    def create_widgets(self):
        """Create the widgets for the App."""
        self.main_frame = MainFrame(self)
        # Make the main frame expand to fill the root
        self.main_frame.grid(row=0, column=0, sticky="nsew")

        # Make the main frame expand to fill the root
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)


if __name__ == "__main__":
    app = App()
    app.mainloop()