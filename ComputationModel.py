import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from pydub import AudioSegment

# Use to create a mono-channel wav file from another audio file. Avoids metadata and bit depth problems for scipy
def CreateTempWav(filename):
    # returns name of temp file, always "temp.wav"
    asTemp = AudioSegment.from_file(filename)
    asTemp.set_channels(1).export("temp.wav", format="wav")
    return "temp.wav"

# Loads an audio file, getting samplerate and raw data
def LoadData(filename):
    # Returns samplerate and an array of data

    # Checks if temp file is needed
    if filename[-4:] != ".wav":
        # File isn't wav, convert it
        filename = CreateTempWav(filename)
    else:
        asTest = AudioSegment.from_file(filename)
        if asTest.channels != 1:
            # Not mono-channel, remake file
            filename = CreateTempWav(filename)

    try:
        samplerate, data = wavfile.read(filename)
    except ...:
        # scipy couldn't handle wav file, remake it with pydub
        CreateTempWav(filename)
        samplerate, data = wavfile.read("temp.wav")

    print(f"Loaded {filename} with length of {data.shape[0] / samplerate} seconds")

    return samplerate, data

# Calculates resonant frequency (frequency of the highest amplitude)
def CalculateResonantFrequency(spectrum, freqs):
    return freqs[np.unravel_index(np.argmax(spectrum), spectrum.shape)[0]]

# Calculates amplitudes at various time points for each frequency. Also make spectrogram
def CalculateFrequencies(samplerate, data):
    # Create amplitude data for frequencies. Returns 2D array data, 1D array of frequencies, 1D array of timepoints,
    # and image of graph
    spectrum, freqs, t, im = plt.specgram(data, Fs=samplerate, NFFT=1024, cmap=plt.get_cmap('autumn_r'))
    print(f"Resonant frequency is {CalculateResonantFrequency(spectrum, freqs)} Hz")
    return spectrum, freqs, t, im

# Find the closest frequency above minimum
def SearchClosestGreater(freqs, minimum):
    # Returns value of frequency
    return min(filter(lambda a: a > minimum, freqs))

# Gets data for specific frequencies of spectrum
def GetLowMedHighData(spectrum, freqs):
    # return amplitude data for low freq, data for med freq, and data for high freq

    # sample frequencies to test
    lowFreq = SearchClosestGreater(freqs, 100)
    medFreq = SearchClosestGreater(freqs, 1000)
    highFreq = SearchClosestGreater(freqs, 6000)

    # Gets spectrum data for each sample frequency
    return spectrum[np.nonzero((freqs == lowFreq))[0][0]], \
        spectrum[np.nonzero((freqs == medFreq))[0][0]], \
        spectrum[np.nonzero((freqs == highFreq))[0][0]]

# Converts array of amplitudes to decibels
def ConvertAmpToDec(ampData):
    # warning when amplitude is 0. Matplot also warns too, so not important to fix
    return 10 * np.log10(ampData)

# Computes max volume time and RT60
def ComputeRT60(decData, t):
    # returns time when max decibels and length of time for rt60
    maxI = np.argmax(decData)
    dif5 = np.abs(decData[maxI:] - (decData[maxI] - 5)).argmin()
    dif25 = np.abs(decData[maxI:] - (decData[maxI] - 25)).argmin()
    rt20 = t[maxI + dif25] - t[maxI + dif5]
    return t[maxI], (rt20 * 3)
