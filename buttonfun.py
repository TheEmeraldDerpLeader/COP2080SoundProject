"""
Button functions used throughout GUI
Create audio file object
combine plots
Toggle between plots displayed
Creation of additional graph
"""

from tkinter import *
from tkinter import filedialog, Button, ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from ComputationModel import *

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
        self.canvas = None
        self.canvas_widget = None

    def load_audio(self):
        """
        Grabs audio files path
        Use the load data function from ComputationModel.py
        This will ensure the usability of all audio files
        """
        ButtonFunction.filePath = filedialog.askopenfilename()

    def graphTitle(self):
        # Plot title and horizontal separator
        text = Label(text=self.title)
        text.grid(row=3, columnspan=10, sticky="ew")
        horizontalSeparator = ttk.Separator(orient="horizontal")
        horizontalSeparator.grid(row=4, columnspan=6, sticky="ew")
        pass

    def displayStaticits(self):
        # Add a separator and display RT60 values
        horizontalSeparator = ttk.Separator(orient="horizontal")
        horizontalSeparator.grid(row=7, columnspan=6, sticky="ew")

        # Get the frequency and time data from the waveform
        sample_rate, data = LoadData(ButtonFunction.filePath)
        _, frequency, time, _ = CalculateFrequencies(sample_rate, data)

        frequencyText = Label(text=f"Highest Resonance frequency: {max(frequency)}", bg="light gray")
        frequencyText.grid(row=8, column=0, columnspan=3)
        timeText = Label(text=f"Max time: {max(time)}", bg="light gray")
        timeText.grid(row=8, column=3, columnspan=3)

        horizontalSeparator2 = ttk.Separator(orient="horizontal")
        horizontalSeparator2.grid(row=9, columnspan=6, sticky="ew")
        pass

    def displayOGWave(self):
        """
        Plot the wave
        RT60
        """
        self.graphTitle()

        # Embed graph
        # Get the audio data
        frame_rate, signal = LoadData(ButtonFunction.filePath)

        # Create a time array
        time = np.linspace(0, len(signal) / frame_rate, num=len(signal))

        # Plot the waveform
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.plot(time, signal, color='b')
        ax.set_xlabel('Time (seconds)')
        ax.set_ylabel('Amplitude')
        ax.set_title('Original Waveform')

        # Embed the plot in Tkinter window
        self.canvas = FigureCanvasTkAgg(fig)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.grid(row=6, columnspan=6, sticky="ew")

        # RT60 Values
        self.displayStaticits()
        pass

    def cycle(self):

        pass
    def sixthplot(self):
        print(self.filepath)
        pass
