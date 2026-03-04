from tkinter import *
import all_constants as c
import conversion_rounding as cr
from functools import partial # To prevent unwanted windows
from datetime import date



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
            ["History / Export", "#004c99", self.to_history, 1, 1],
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

        # Name to help button and to history button
        self.to_help_button = self.button_ref_list[2]

        # retrieve 'history / export' button and disable it at the start
        self.to_history_button = self.button_ref_list[3]
        self.to_history_button.config(state=DISABLED)


    def to_help(self):
        """
        Opens dialogue box and disables help button
        (so that users can't create multiple help tabs)
        """
        DisplayHelp(self)


    def to_history(self):
        """
        Opens dialogue box and disables history button
        (so that users can't create multiple history tabs)
        """
        HistoryExport(self, self.all_calculations_list)


    def check_temp(self, min_temp):
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
To use the program, simply enter the temperature you wish to convert and then choose to convert to either degrees Celsius (centigrade) or Fahrenheit...

Note that -273 degrees C (-459 F) is absolute zero (the coldest possible temperature). If you try to convert a temperature that is less than -273 degrees C, you will get an error message.

To see your calculation history and export it to a text file, please click the 'History/Export' button.
        """

        self.help_text_label = Label(self.help_frame,
                                     text=help_text, wraplength=350,
                                     justify="left")
        self.help_text_label.grid(row=1, padx=10)

        self.dismiss_button = Button(self.help_frame,
                                     font=("Arial", 12, "bold"),
                                     text="Dismiss", bg="#CC6600",
                                     fg="#FFFFFF",
                                     command=partial(self.close_help, partner))
        self.dismiss_button.grid(row=2, padx=10, pady=10)

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


class HistoryExport:
    """
    Displays history dialogue box
    """

    def __init__(self, partner, calculations):
        # setup dialogue box
        self.history_box = Toplevel()

        # Disable history button
        partner.to_history_button.config(state=DISABLED)

        # if users press cross at the top, coses history and
        # 'releases' history button
        self.history_box.protocol("WM_DELETE_WINDOW",
                               partial(self.close_history, partner))

        self.history_frame = Frame(self.history_box)
        self.history_frame.grid()

        #background color and text for calculation area
        if len(calculations) <= c.Max_CALCS:
            calc_back = "#D5E8D4"
            calc_amount = "all your"

        else:
            calc_back = "#FFE6Cc"
            calc_amount = f"showing {c.Max_CALCS} / {len(calculations)}"

        # strings for 'long' labels
        recent_intro_text = (f"bellow are your recent calculations - {calc_amount} all calculations are "
                             f"shown to the nearest degree")

        # create string from calculations list (newest calculations first)
        newest_first_string = ""
        newest_first_list = list(reversed(calculations))

        # last item added in outside the for loop so that the pacing is correct
        if len(newest_first_list) <= c.Max_CALCS:

            for item in newest_first_list[:-1]:
                newest_first_string += item + "\n"

            newest_first_string += newest_first_list[-1]

        # If we have more than Five items...
        else:
            for item in newest_first_list[:c.Max_CALCS-1]:
                newest_first_string += item + "\n"

            newest_first_string += newest_first_list[c.Max_CALCS-1]

        export_instruction_txt = ("please push <Export> to save your calculations in "
                                  "file. If the filename already exists, it will be replaced")

        # label list (label txt | format | bg)
        history_labels_list = [
            ["History / Export", "Arial 16 bold", None],
            [recent_intro_text, "Arial 11", None],
            [newest_first_string, "Arial 14", calc_back],
            [export_instruction_txt, "Arial 11", None],
        ]

        history_label_ref = []
        for count, item in enumerate(history_labels_list):
            make_label = Label(self.history_box, text=item[0],
                               bg=item[2],
                               wraplength=300, justify="left", pady=10, padx=20)
            make_label.grid(row=count)

            history_label_ref.append(make_label)

        #retrive export instruction label so we can
        # configure it to show the filename if the user exports the file
        self.export_filename_label = history_label_ref[3]

        # make frame to hold buttons (two columns)
        self.hist_button_frame = Frame(self.history_box)
        self.hist_button_frame.grid(row=4)

        # button list (button text | bg color | command | row | column)
        button_details_list = [
            ["Export", "#004c99", partial(self.export_to_file, partner, calculations), 0, 0],
            ["Close", "#666666", partial(self.close_history, partner), 0, 1],
        ]



        for btn in button_details_list:
            self.make_button = Button(self.hist_button_frame,
                                      font=("Arial", 12, "bold"),
                                      text=btn[0], bg=btn[1],
                                      fg="#ffffff", width=12,
                                      command=btn[2])
            self.make_button.grid(row=btn[3], column=btn[4], padx=10, pady=10)


    def export_to_file(self, partner, calculations):
        """
        Exports calculations to file
        """
        # Get current date for heading and filename
        today = date.today()

        # Get day, month and year as individual strings
        day = today.strftime("%d")
        month = today.strftime("%m")
        year = today.strftime("%Y")

        # file_name = f"temperatures_{day}_{month}_{year}"
        file_name = f"temperatures_{day}_{month}_{year}"

        success_string = (f"Export successful! the file is called: "
                          f"{file_name}.txt")
        self.export_filename_label.config(fg="#009900", text=success_string,
                                          font=("Arial", 12, "bold"))

        write_to = f"{file_name}.txt"

        with open(write_to, "w") as text_file:
            text_file.write("***** Temperature Calculation *****\n")
            text_file.write(f"Generated: {day}/{month}/{year}\n\n")
            text_file.write("Here is your calculation history (oldest to newest)...\n")

            # write the item to file
            for item in calculations:
                text_file.write(item)
                text_file.write("\n")


    def close_history(self, partner):
        """
        Closes history dialogue box (and enables history button)
        """
        # Put history button back to normal...
        partner.to_history_button.config(state=NORMAL)
        self.history_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
