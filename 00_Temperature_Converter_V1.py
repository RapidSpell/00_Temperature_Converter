from tkinter import *


class Converter:
    """
    Temperature conversion tool ( Celsius to Fahrenheit or vice versa )
    """

    def __init__(self):
        """
        Temperature converter GUI
        """

        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.temp_heading = Label(self.temp_frame,
                                  text="Temperature Converter",
                                  font="Arial 16 bold"
                                  )
        self.temp_heading.grid(row=0)

        instructions = ("please enter a temperature below and then press"
                        "one of the buttons to convert it from centigrade"
                        "to Fahrenheit.")
        self.temp_instructions = Label(self.temp_frame,
                                       text=instructions,
                                       wraplength=250, width=40,
                                       justify="left")
        self.temp_instructions.grid(row=1)

        self.temp_entry = Entry(self.temp_frame,
                                font="Arial 14"
                                )
        self.temp_entry.grid(row=2, padx=10, pady=10)

        error = "Please enter a number"
        self.temp_error = Label(self.temp_frame, text=error,
                                fg="#9C0000",
                                font="Arial 16")
        self.temp_error.grid(row=3)

        #conversion, help and history / export button
        self.button_fame = Frame(self.temp_frame)
        self.button_fame.grid(row=4)

        self.to_celsius_button = Button(self.button_fame,
                                    text="To Degrees C",
                                    bg="#990099",
                                    fg="#ffffff",
                                    width=12
                                    )
        self.to_celsius_button.grid(row=0, column=0, padx=5, pady=5)

        self.to_fahrenheit_button = Button(self.button_fame,
                                        text="To Fahrenheit",
                                        bg="#009900",
                                        fg="#ffffff",
                                        width=12
                                        )
        self.to_fahrenheit_button.grid(row=0, column=1, padx=5, pady=5)

        self.help_button = Button(self.button_fame,
                                   text="Help / Info",
                                   bg="#cc6600",
                                   fg="#ffffff",
                                   width=12
                                  )
        self.help_button.grid(row=1, column=0, padx=5, pady=5)

        self.history_button = Button(self.button_fame,
                                  text="History / Export",
                                  bg="#004c99",
                                  fg="#ffffff",
                                  width=12
                                  )
        self.history_button.grid(row=1, column=1, padx=5, pady=5)



    # main routine


if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()

