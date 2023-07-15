"""This tkinter frame is the main frame of the application."""
import tkinter as tk
from tkinter import ttk


class MainFrame(ttk.Frame):
    """This tkinter frame is the main frame of the application."""
    
    def __init__(self, parent, controller):
        """Initialize the MainFrame."""
        super().__init__(parent)
        self.controller = controller
        
        # Make the main frame expand to fill the root
        self.grid(row=0, column=0, sticky="nsew")
        # Change main frame's border color to yellow for visibility
        self.configure(borderwidth=5, relief="groove")
        self.create_widgets()

    def create_widgets(self):
        """Create the widgets for the MainFrame."""
        self.master.title("Techwriter's AI")
        self.master.geometry("800x600")
        # Add a label to the frame
        self.system_label = ttk.Label(self, text="System: ")
        # Add an entry field to the frame
        self.system_text = tk.Text(self, height=10, wrap="word")
        # Add a scrollbar to the entry field
        self.system_scroll = ttk.Scrollbar(self, orient="vertical", command=self.system_text.yview)
        # Add a button to the frame
        self.prompt_button = ttk.Button(self, text="Prompt", command=self.controller)

        # Add the widgets to the frame
        self.system_label.grid(row=0, column=0, sticky="n")
        self.system_text.grid(row=0, column=1, sticky="nsew")
        self.system_scroll.grid(row=0, column=1, sticky="nse")
        self.prompt_button.grid(row=0, column=2, sticky="nsew")

        # make the entry field expand to fill the frame
        self.system_text.grid_rowconfigure(0, weight=1)
        self.system_text.grid_columnconfigure(0, weight=1)
        self.system_text.configure(yscrollcommand=self.system_scroll.set)

        # make the frame expand to fill the root
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

if __name__ == "__main__":
    root = tk.Tk()
    controller = lambda: print("Hello World!")
    main_frame = MainFrame(root, controller)
    main_frame.pack(fill="both", expand=True)    
    root.mainloop()