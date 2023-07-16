"""This controller module contains the controller classes for the input prompts.
This controls the input prompts for the system, user, and assistant roles."""


class InputController():
    """This controller class contains the controller methods for the input prompts."""

    def __init__(self, label_text: str = "System"):
        """Initialize the InputController."""
        self.label_text = label_text

    def __call__(self):
        """Call the InputController."""
        print(f'{self.label_text}: Hello World!')