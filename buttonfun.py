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
        self.counter = 0

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
        horizontalSeparator.grid(row=4, columnspan=10, sticky="ew")
        pass

    def displayStaticits(self):
        # Add a separator and display RT60 values
        horizontalSeparator = ttk.Separator(orient="horizontal")
        horizontalSeparator.grid(row=7, columnspan=10, sticky="ew")

        # Get the frequency and time data from the waveform
        sample_rate, data = LoadData(ButtonFunction.filePath)
        _, frequency, time, _ = CalculateFrequencies(sample_rate, data)

        frequencyText = Label(text=f"Highest Resonance frequency: {max(frequency)}", bg="light gray")
        frequencyText.grid(row=8, column=0, columnspan=2)
        timeText = Label(text=f"Max time: {max(time)}", bg="light gray")
        timeText.grid(row=8, column=3, columnspan=2)

        horizontalSeparator2 = ttk.Separator(orient="horizontal")
        horizontalSeparator2.grid(row=9, columnspan=10, sticky="ew")
        pass

    def displayOGWave(self):
        """
        Plot the wave
        RT60
        """
        self.graphTitle()

        # Embed graph
        # Get the audio data
        sample_rate, data = LoadData(ButtonFunction.filePath)
        time = np.linspace(0, len(data) / sample_rate, num=len(data))

        # Plot the waveform
        fig, ax = plt.subplots(figsize=(5, 4))
        ax.plot(time, data, color='b')
        ax.set_xlabel('Time (seconds)')
        ax.set_ylabel('Amplitude')
        ax.set_title('Original Waveform')

        # Embed the plot in Tkinter window
        self.canvas = FigureCanvasTkAgg(fig)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.grid(row=6, columnspan=10, sticky="ew")

        pass

    def cycle(self):
        # Get data for frequencies
        sample_rate, data = LoadData(ButtonFunction.filePath)
        spectrum, frequencies, t, im = CalculateFrequencies(sample_rate, data)
        lowArray, medArray, highArray = GetLowMedHighData(spectrum, frequencies)

        fig, ax = plt.subplots(figsize=(5, 4))
        # Check to see which frequency to show
        # copy from here
        if self.counter % 3 == 0:
            # Plot the waveform
            ax.plot(t, lowArray, color='b')
            ax.set_title('Low Frequency Waveform')

            decD = ConvertAmpToDec(lowArray)
            startT, rtT = ComputeRT60(decD, t)

            frequencyText = Label(text=f"RT60: {rtT}", bg="light gray")
            frequencyText.grid(row=8, column=0, columnspan=3)
            timeText = Label(text=f"Max time: {max(t)}", bg="light gray")
            timeText.grid(row=8, column=3, columnspan=3)
        elif self.counter % 3 == 1:
            # Plot the waveform
            ax.plot(t, medArray, color='r')
            ax.set_title('Medium Frequency Waveform')
            decD = ConvertAmpToDec(medArray)
            startT, rtT = ComputeRT60(decD, t)

            frequencyText = Label(text=f"RT60: {rtT}", bg="light gray")
            frequencyText.grid(row=8, column=0, columnspan=3)
            timeText = Label(text=f"Max time: {max(t)}", bg="light gray")
            timeText.grid(row=8, column=3, columnspan=3)
        else:
            ax.plot(t, highArray, color='g')
            ax.set_title('High Frequency Waveform')
            decD = ConvertAmpToDec(highArray)
            startT, rtT = ComputeRT60(decD, t)

            frequencyText = Label(text=f"RT60: {rtT}", bg="light gray")
            frequencyText.grid(row=8, column=0, columnspan=3)
            timeText = Label(text=f"Max time: {max(t)}", bg="light gray")
            timeText.grid(row=8, column=3, columnspan=3)
        # to here
        ax.set_xlabel('Time (seconds)')
        ax.set_ylabel('Amplitude')

        # Embed the plot in Tkinter window
        self.canvas = FigureCanvasTkAgg(fig)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.grid(row=6, columnspan=6, sticky="ew")

        self.counter += 1
        pass

    def displayCombined(self):
        # Get data for frequencies
        sample_rate, data = LoadData(ButtonFunction.filePath)
        spectrum, frequencies, t, im = CalculateFrequencies(sample_rate, data)
        lowArray, medArray, highArray = GetLowMedHighData(spectrum, frequencies)

        # Create a time array
        fig, ax = plt.subplots(figsize=(5, 4))
        ax.plot(t, lowArray, color='r')
        ax.plot(t, medArray, color='g')
        ax.plot(t, highArray, color='b')

        ax.set_xlabel('Time (seconds)')
        ax.set_ylabel('Frequency')
        ax.set_title('Combined Frequency Graph')

        self.canvas = FigureCanvasTkAgg(fig)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.grid(row=6, columnspan=6, sticky="ew")

        pass

    def sixthplot(self):
        """
        Plot the wave
        RT60
        """
        self.graphTitle()

        # Embed graph
        # Get the audio data
        frame_rate, signal = LoadData(ButtonFunction.filePath)

        # Plot the waveform
        fig, ax = plt.subplots(figsize=(5, 4))
        ax.set_xlabel('Time (seconds)')
        ax.set_ylabel('Frequencies')
        ax.set_title('Spectrogram')

        # Embed the plot in Tkinter window
        self.canvas = FigureCanvasTkAgg(fig)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.grid(row=6, columnspan=10, sticky="ew")

        self.displayStaticits()