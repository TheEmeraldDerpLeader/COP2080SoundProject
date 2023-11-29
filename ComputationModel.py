import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

from pydub import AudioSegment

#To Do:
# 1: Set up functions to load file, only recreating wav files if (\ don't work D: )
#they are multi-channel or fail to load. might be function/controller/noah task
# 2: Compute resonance and frequency (from data)
# 3: Get low, med, high freq data
# 4: Compute RT60
# 5: show spectogram function for extra button maybe


# Use to create a mono-channel wav file from another audio file. Avoids metadata and bit depth problems for scipy
def CreateTempWav(filename):
    asTemp = AudioSegment.from_file(filename)
    asTemp.set_channels(1).export("temp.wav", format="wav")

audioFile = "SmurfMushroomCat.ogg"
#audioTest = "test.wav"
audioTest = "problemTest.wav"

asSong = AudioSegment.from_file(audioFile)
#asSong.export(audioTest, format="wav")

asTest = AudioSegment.from_file(audioTest)
print(asTest.channels)
asTest = asTest.set_channels(1)
print(asTest.channels)
#asTest.export(audioTest, format="wav")

try:
    samplerate, data = wavfile.read(audioTest)
except:
    CreateTempWav(audioTest)
    samplerate, data = wavfile.read("temp.wav")
    pass

# Only works when stereo, mono wav files give 1D data, so shape only describes length
#print(f"number of channels = {data.shape[len(data.shape) - 1]}")
print(data.shape[0])
print(f"sample rate = {samplerate}Hz")
length = data.shape[0] / samplerate
print(f"length = {length}s")

#plotting spectrogram
#spectrum, freqs, t, im = plt.specgram(data, Fs=samplerate, \
#NFFT=1024, cmap=plt.get_cmap('autumn_r'))
#cbar = plt.colorbar(im)
#plt.xlabel('Time (s)')
#plt.ylabel('Frequency (Hz)')
#cbar.set_label('Intensity (dB)')
#plt.show()