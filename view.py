"""
Create a GUI that displays 4 graphs: Displays one graph at a time.
1. Original Waveform
2. Cycle Through Low, Medium, High Frequencies
3. Combined Waveform
4. Sixth data plot
Displays the RT60 values under the graphs
Toolbar:
1. Open File Button
2. Display Original Waveform
3. Combine Graphs Button
4. Cycle through low, medium, high frequency graphs
5. Display combined waveform
6. Sixth data plot
Graphs:
Display Graphs in Grid formation with RT60 values listed directly below them
"""
import tkinter as tk
from tkinter import Menu

# create the window
root = tk.Tk()
root.title("CSP Sound Project")
root.resizable(False, False)
root.geometry('800x600')
root.config(bg='gray')

# Top Tool Bar:
menubar = Menu()

openButton = Menu(menubar, tearoff=False)
menubar.add_cascade(label="Open")
openButton.add_command(label="Open")

combineButton = Menu(menubar, tearoff=False)
menubar.add_cascade(label="Combine")
combineButton.add_command(label="Combine")

originalButton = Menu(menubar, tearoff=False)
menubar.add_cascade(label="Disp Original")
originalButton.add_command(label="Disp Original")

cycleButton = Menu(menubar, tearoff=False)
menubar.add_cascade(label="Cycle")
cycleButton.add_command(label="Cycle")

dispCombinedButton = Menu(menubar, tearoff=False)
menubar.add_cascade(label="Disp Combined")
dispCombinedButton.add_command(label="Disp Combined")

# Configure the root such that it displays the menubar in the application
root.config(menu=menubar)

# run the application
root.mainloop()
