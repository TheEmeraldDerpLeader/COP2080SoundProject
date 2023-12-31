"""
Create a GUI that displays 4 graphs: Displays one graph at a time.
1. Original Waveform
2. Cycle Through Low, Medium, High Frequencies
3. Combined Waveform
4. Spectrogram data plot
Displays the RT60 values under the graphs
Toolbar:
1. Open File Button
2. Display Original Waveform
3. Cycle through low, medium, high frequency graphs
4. Display combined waveform
5. Spectrogram data plot
Graphs:
Display Graphs in Grid formation with RT60 values listed directly below them
"""
import tkinter as tk
from tkinter import ttk
from buttonfun import ButtonFunction

# create the window
root = tk.Tk()
root.title("CSP Sound Project")
root.resizable(True, True)
root.geometry('809x475')
root.config(bg='light gray')

"""
Button Event:
On hover, change the button color
On leave, return to default color
"""
def onHover(event):
    event.widget.config(bg="gray")

def onLeave(event):
    event.widget.config(bg="SystemButtonFace")


"""
All buttons aligned in a single tool bar along the top of the application
"""
# Open file button
# Make a button object from buttonFun.py
openButton = ButtonFunction("Open File")
openButton.grid(row=0, column=0, ipadx=37.5)
openButton.configure(command=openButton.load_audio)
openButton.bind("<Enter>", onHover)
openButton.bind("<Leave>", onLeave)

# Display OG function button
displayOGButton = ButtonFunction("Dsp OG Wave")
displayOGButton.grid(row=0, column=1, ipadx=37.5)
displayOGButton.bind("<Enter>", onHover)
displayOGButton.bind("<Leave>", onLeave)
displayOGButton.configure(command=displayOGButton.displayOGWave)

# Cycle button
cycleButton = ButtonFunction("Cycle")
cycleButton.grid(row=0, column=3, ipadx=37.5)
cycleButton.bind("<Enter>", onHover)
cycleButton.bind("<Leave>", onLeave)
cycleButton.configure(command=cycleButton.cycle)
# cycleButton.configure(command=cycleButton.create_plot)

# Display combined waveform button
dispCombinedButton = ButtonFunction("Dsp Combined Waves")
dispCombinedButton.grid(row=0, column=4, ipadx=37.5)
dispCombinedButton.bind("<Enter>", onHover)
dispCombinedButton.bind("<Leave>", onLeave)
dispCombinedButton.configure(command=dispCombinedButton.displayCombined)

# Sixth plot
spectrogram = ButtonFunction("Spectrogram Button")
spectrogram.grid(row=0, column=5, ipadx=37.5)
spectrogram.bind("<Enter>", onHover)
spectrogram.bind("<Leave>", onLeave)
spectrogram.configure(command=spectrogram.sixthPlot)

horizontalSeparator = ttk.Separator(root, orient="horizontal")
horizontalSeparator.grid(row=2, columnspan=10, sticky="ew")

# run the application
root.mainloop()
