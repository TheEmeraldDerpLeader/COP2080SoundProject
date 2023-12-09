# Change Log for Grant's Branch

## Version 00.002.02

### Audio
- Changed/fixed resonant frequency calculations
- Used fixed values for low med high frequencies instead of proportions of max


### Other
- Removed leftover debug print

## Version 00.002.01

### Audio
- Fixed rt60, doesn't always work with unlucky data, but that's how it's implemented in the slides

## Version 00.002.00
Created functions and stuff for most model stuff

### Audio
Finished and verified functions to load data, get spectrogram, get frequencies, etc...

- Functions to load and convert files so scipy can create raw data from them
- Functions to get data for amplitudes and frequencies
- Function to convert amplitude data into decibels
- Function to calculate RT60 (might be wrong, see comments)

### Other
- Testing code is moved into a main check
- Cleaned up testing code
- Added Cave14.ogg test file, has face in spectrogram
- Added ReverbFart.ogg test file

## Version 00.001.00
Started audio loading and manipulation

### Audio
Started working on functions and implementations for loading and converting files for scipy to use

- Function to create a wav file from an audio file that scipy should guarenteed be able to use
- Example of checking if scipy fails to load file
- Tested loading and writing files 

### Other
- Added code for spectrogram plot (currently commented)