from tkinter import *
from functools import partial # To prevent unwanted windows
import all_constants as c
import conversion_rounding as cr


class Converter:
    """
    Temperature conversion tool ( Celsius to Fahrenheit or vice versa )
    """

    def __init__(self):
        """
        Temperature converter GUI
        """

        self.all_calculations_list = []

        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.temp_heading = Label(self.temp_frame,
                                  text="Temperature Converter",
                                  font="Arial 16 bold"
                                  )
        self.temp_heading.grid(row=0)

        instructions = ("please enter a temperature below and then press"
                        "one of the buttons to convert it from centigrade"
                        "to Fahrenheit or vice versa.")
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
        self.answer_error = Label(self.temp_frame, text=error,
                                  fg="#004c99",
                                  font="Arial 16")
        self.answer_error.grid(row=3)

        #conversion, help and history / export button
        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)

        # button list (button text | bg color | row | column)
        button_details_list = [
            ["To Celsius", "#990099", lambda:self.check_temp(c.ABS_ZERO_FAHRENHEIT), 0, 0],
            ["To Fahrenheit", "#009900", lambda:self.check_temp(c.ABS_ZERO_CELSIUS), 0, 1],
            ["Help / info", "#cc6600", self.to_help, 1, 0],
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

        # retrieve to_helpbutton
        self.to_help_button = self.button_ref_list[2]

        # retrieve 'history / export' button and disable it at the start
        self.to_history_button = self.button_ref_list[3]
        self.to_history_button.config(state=DISABLED)

    def check_temp(self,min_temp):
        # retrieve temperature to be converted
        to_convert = self.temp_entry.get()

        #checks that amount to be converted is a number above absolute zero
        try:
            to_convert = float(to_convert)
            if to_convert >= min_temp:
                error = ""
                self.convert(min_temp, to_convert)

            else:
                error= f"please enter a number {min_temp} or above"

        except ValueError:
            error = "please enter a number"

        if error != "":
            self.answer_error.config(text=error, fg="#9c0000")
            self.temp_entry.config(bg="#f4CCCC")

        else:
            self.answer_error.config(fg="#004c99")
            self.temp_entry.config(bg="#ffffff")

        self.temp_entry.delete(0, END)


    def convert(self, min_temp, to_convert):

        if min_temp == c.ABS_ZERO_CELSIUS:
            answer = cr.to_fahrenheit(to_convert)
            answer_statement = f"{to_convert}°C is {answer}°F"
            self.answer_error.config(text=f"{to_convert}°C is {answer}°F")

        else:
            answer = cr.to_celsius(to_convert)
            answer_statement = f"{to_convert}°F is {answer}°C"

        # Enable history_button as soon as we have a valid calculation
        self.to_history_button.config(state=NORMAL)

        self.answer_error.config(text=answer_statement, fg="#004c99")
        self.all_calculations_list.append(answer_statement)
        print(self.all_calculations_list)


    def to_help(self):
        """
        Opens dialogue box and disables help button
        (so that users can't create multiple help tabs)
        """
        DisplayHelp(self)


class DisplayHelp:

    def __init__(self, partner):

        # setup dialogue box and background color
        background = "#FFE6CC"
        self.help_box = Toplevel()

        # Disable help button
        partner.to_help_button.config(state=DISABLED)

        # if users press cross at the top, coses help and
        # 'releases' help button
        self.help_box.protocol("WM_DELETE_WINDOW",
                               partial(self.close_help, partner))

        self.help_frame = Frame(self.help_box,
                                height=200)
        self.help_frame.grid()

        self.help_heading_label = Label(self.help_frame,
                                        text="Help / Info",
                                        font=("Arial", 14, "bold"),)
        self.help_heading_label.grid(row=0)

        help_text = """
To use the program, simply enter the temperature you wish to convert and them choose to convert to ether Celsius (centigrade) or Fahrenheit...

Note that -273 degrees C (-459 F) is absolute zero (the coldest possible temperature). if you try to convert a temperature that is bellow absolute zero you will get an error message.

To see your calculation history and export it to a text file, please click the 'History / Export' button.
        """

        self.help_text_label = Label(self.help_frame,
                                     text=help_text, wraplength=350,
                                     font="arial 10",
                                     justify="left")
        self.help_text_label.grid(row=1, padx=10)

        self.dismiss_button = Button(self.help_frame,
                                     font=("Arial", 12, "bold"),
                                     text="Dismiss", bg="#CC6600",
                                     fg="#FFFFFF",
                                     command=partial(self.close_help, partner))
        self.dismiss_button.grid(row=2, padx=10)

        # List and loop to set background color on
        # everything except the buttons
        recolor_list = [self.help_frame, self.help_heading_label,
                        self.help_text_label]

        for item in recolor_list:
            item.config(bg=background)


    def close_help(self, partner):
        """
        Closes help dialogue box (and enables help button)
        """
        # Put help button back to normal...
        partner.to_help_button.config(state=NORMAL)
        self.help_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
