"""
Button functions used throughout GUI
Create audio file object
combine plots
Toggle between plots displayed
Creation of additional graph
"""

from tkinter import *
from tkinter import filedialog, Button, ttk

# window.mainloop()


class ButtonFunction(Button):
    def __init__(self, txt):
        super().__init__(text=txt, activebackground="light blue", relief=FLAT)
        self.title = txt
        """
        Construct Button_Function object
        """
        self.my_text = Text(font=("helvetica", 16))
        self.open_button = Button(text="Open Audio File", command=self.load_audio)
        self.filepath = ""

    def load_audio(self):
        """
        Grabs audio files path
        Mutates self.filepath
        """
        # find file path for audio file

        self.filepath = filedialog.askopenfilename()
        # text_file = open(self.filepath, 'r')
        stuff = self.filepath
        self.create_plot()
        self.my_text.insert(END, stuff)
        # text_file.close()

    def create_plot(self):
        """
        Add plot title
        Plot the wave
        RT60, RT40, RT20
        """
        text = Label(text=self.title)
        text.grid(row=3, columnspan=10, sticky="ew")
        horizontalSeparator = ttk.Separator(orient="horizontal")
        horizontalSeparator.grid(row=4, columnspan=6, sticky="ew")
        pass


# if __name__ == "__main__":
#     window = Tk()
#     window.title('Module test')
#     window.iconbitmap('/text.txt')
#     window.geometry("500x450")
#     # Creates button functions object containing several
#     # GUI elements to pack into root window
#     # Includes, file button, graph button, graphs and maybe toggle
#     buttons = ButtonFunction()
#     buttons.my_text.pack(pady=20)
#     buttons.open_button.pack(pady=20)
#     window.mainloop()

