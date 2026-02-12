from tkinter import *

from attr.validators import disabled


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
        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)

        # button list (button text | bg color | row | column)
        button_details_list = [
            ["To Celcius", "#990099", "", 0, 0],
            ["To Fahrenheit", "#009900", "", 0, 1],
            ["Help / info", "#cc6600", "", 1, 0],
            ["History / Export", "#004c99", "", 1, 1],
        ]

        # list to hold buttons oce they have been made
        self.button_ref_list = []

        for item in button_details_list:
            self.make_button = Button(self.button_frame,
                                      text=item[0], bg=item[1],
                                      fg="#ffffff", font="Arial 12 bold",
                                      width=12, command=item[2])
            self.make_button.grid(row=item[3], column=item[4], padx=5, pady=5)

            self.button_ref_list.append(self.make_button)

        # retrieve 'history / export' button and disable it at the start
        self.to_history_button = self.button_ref_list[3].config(state=DISABLED)


    # main routine

if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()

