from tkinter import *
from functools import partial # To prevent unwanted windows
import all_constants as c


class Converter:
    """
    Temperature conversion tool (C to F or F to C)
    """

    def __init__(self):
        """
        Temperature converter GUI
        """

        self.all_calculations_list = ['10.0°F is -12°C', '20.0°F is -7°C',
                                      '30.0°F is -1°C', '40.0°F is 4°C',
                                      '60.0°F is 16°C']

        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.to_history_button = Button(self.temp_frame,
                                     text="History / Export",
                                     bg="#CC6600",
                                     fg="#FFFFFF",
                                     font=("Arial", 14, "bold"),
                                     width=12,
                                     command=self.to_history)
        self.to_history_button.grid(row=0, padx=5, pady=5)


    def to_history(self):
        """
        Opens dialogue box and disables history button
        (so that users can't create multiple history tabs)
        """
        HistoryExport(self, self.all_calculations_list)


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
            ["Export", "#004c99", "", 0, 0],
            ["Close", "#666666", partial(self.close_history, partner), 0, 1],
        ]



        for btn in button_details_list:
            self.make_button = Button(self.hist_button_frame,
                                      font=("Arial", 12, "bold"),
                                      text=btn[0], bg=btn[1],
                                      fg="#ffffff", width=12,
                                      command=btn[2])
            self.make_button.grid(row=btn[3], column=btn[4], padx=10, pady=10)


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
