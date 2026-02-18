from tkinter import *
from functools import partial # To prevent unwanted windows


class Converter:
    """
    Temperature conversion tool (C to F or F to C)
    """

    def __init__(self):
        """
        Temperature converter GUI
        """

        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.to_help_button = Button(self.temp_frame,
                                     text="Help / Info",
                                     bg="#CC6600",
                                     fg="#FFFFFF",
                                     font=("Arial", 14, "bold"),
                                     width=12,
                                     command=self.to_help)
        self.to_help_button.grid(row=0, padx=5, pady=5)


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
help text goes here
and here
and here
and more
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


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
