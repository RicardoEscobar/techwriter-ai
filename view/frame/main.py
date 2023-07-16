"""This tkinter frame is the main frame of the application."""
import tkinter as tk
from tkinter import ttk

from view.frame.input import InputFrame
from view.frame.source_code import SourceCodeFrame


class MainFrame(ttk.Frame):
    """This tkinter frame is the main frame of the application."""
    
    def __init__(self, parent):
        """Initialize the MainFrame."""
        super().__init__(parent)
        self.master.title("TechWriter AI")
        #self.master.geometry("800x600")
        
        # Make the main frame expand to fill the root
        self.grid(row=0, column=0, sticky="nsew")
        
        # Change main frame's border color to yellow for visibility
        self.configure(borderwidth=5, relief="groove")

        # Creates properties for the source code frame
        self.source_code_frame_text = tk.StringVar()
        self.source_code_frame_text.set("Source Code")
        self.create_widgets()

    def create_widgets(self):
        """Create the widgets for the MainFrame."""
        

        # Add an input frame for the system, user, assistant roles
        self.system_input_frame = InputFrame(self, text="System")
        self.user_input_frame = InputFrame(self, text="User")
        self.assistant_input_frame = InputFrame(self, text="Assistant")

        # Add a source code frame
        frame_title_text = self.source_code_frame_text.get()
        self.source_code_frame = SourceCodeFrame(self, text=frame_title_text)

        # Make the system, user and assistant input frames expand to fill the root horizontally
        self.system_input_frame.grid(row=0, column=0, sticky="ew")
        self.user_input_frame.grid(row=1, column=0, sticky="ew")
        self.assistant_input_frame.grid(row=2, column=0, sticky="nsew")

        # Make the source code frame expand to fill the root horizontally
        self.source_code_frame.grid(row=3, column=0, rowspan=2, sticky="nsew")

        self.system_input_frame.columnconfigure(0, weight=1)
        self.user_input_frame.columnconfigure(0, weight=1)
        self.assistant_input_frame.columnconfigure(0, weight=1)
        
        # Make the main frame expand to fill the root horizontally
        self.columnconfigure(0, weight=1)