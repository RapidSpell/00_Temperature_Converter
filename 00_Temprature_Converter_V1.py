from tkinter import *

class Converter():
    """
    Temperature conversion tool ( Celsius to Fahrenheit or vice versa )
    """

    def __init__(self):
        """
        Temperature converter GUI
        """

        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()


    # main routine


if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()

