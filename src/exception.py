import traceback   
import sys
from src.logger import logging

class MyException(Exception):
    def __init__(self, message):            
        # Call the base class constructor with the parameters it needs
        super().__init__(message)
            
        # Now for your custom code...
        # self.errors = errors
        self.errors = traceback.format_exc()

        logging.error(f"Exception: {message}\nTraceback:\n{self.errors}")

    def __str__(self):
        return f"{super().__str__()}\nTraceback Info:\n{self.errors}"     
    

