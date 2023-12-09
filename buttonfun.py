"""
Button functions used throughout GUI
Create audio file object
combine plots
Toggle between plots displayed
Creation of additional graph
"""

from tkinter import *
from tkinter import filedialog, Button, ttk
import wave
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# window.mainloop()


class ButtonFunction(Button):

    filePath = None

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

        ButtonFunction.filePath = filedialog.askopenfilename()
        # text_file = open(self.filepath, 'r')
        stuff = self.filepath
        self.my_text.insert(END, stuff)

        print(self.filepath)
        # text_file.close()

    def graphTitle(self):
        # Plot title and horizontal separator
        text = Label(text=self.title)
        text.grid(row=3, columnspan=10, sticky="ew")
        horizontalSeparator = ttk.Separator(orient="horizontal")
        horizontalSeparator.grid(row=4, columnspan=6, sticky="ew")
        pass

    def displayReverbTime(self):
        # Add a separator and display RT60 values
        horizontalSeparator = ttk.Separator(orient="horizontal")
        horizontalSeparator.grid(row=7, columnspan=6, sticky="ew")
        pass

    def displayOGWave(self):
        """
        Plot the wave
        RT60
        """
        self.graphTitle()
        # Embedding graph code
        wave_obj = wave.open(ButtonFunction.filePath, 'rb')

        # Get the audio data
        signal = np.frombuffer(wave_obj.readframes(-1), dtype=np.int16)
        frame_rate = wave_obj.getframerate()

        # Create a time array
        time = np.linspace(0, len(signal) / frame_rate, num=len(signal))

        # Plot the waveform
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.plot(time, signal, color='b')
        ax.set_xlabel('Time (seconds)')
        ax.set_ylabel('Amplitude')
        ax.set_title('Waveform Plot')

        # Embed the plot in Tkinter window
        canvas = FigureCanvasTkAgg(fig)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.grid(row=6, columnspan=6, sticky="ew")
        # Load the audio file using librosa
        # RT60 Values
        self.displayReverbTime()
        pass

    def sixthplot(self):
        print(self.filepath)
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

