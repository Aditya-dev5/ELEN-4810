## Capstone project for ELEN-4810 (Digital Signal Processing): I speak Conductor ##
This repository the codebase and supporting files for the project 'I Speak Conductor' (inspired by the character of Lily Aldrin from How I met your mother') which entails enahcing the intelligibility of NYC Subway announcements using 
audio signal processing techniques.

### Files/Folders ###
1. wiener_filt.py: Applies a wiener filter on an input audio signal
2. amplifysig.py: Amplifies the input audio signal using FFT
3. spectrogram.py: Generates spectrogram of an input audio signal
4. bworth_filter.py: Applies a Butterworth filter on an input audio signal
5. Data: Contains input data (.m4a & .wav files)
6. Outputs: Contains output files (.m4a, .wav and .jpg files)
7. Report_I_Speak_Conductor.pdf: The project report document
   
### Requirements: ###
The following modules must be installed in-order to successfully run the .py files
1. numpy
2. scipy
3. matplotlib
4. pydub
5. os

### Steps to run any file 1-4 listed above: ###
1. git clone 
2. Choose a file from the Data/Outputs folder (neglect extension) eg: Penn1 from Data
folder
3. Assign input_path = 'Data' and audio_file_name = 'Penn1'
4. Run

### Note: ### 
The files used for generating plots in the report are namely: 72st, ColumbiaUniversity2,
ColumbiaUniversity5, SalaThai2a, Penn1 and SubwayShort from the Data folder. The
corresponding audio outputs can be found in the Outputs folder eg: h_600_Penn1.wav (output
of the high-pass filter), wiener_11_h_600_Penn1.m4a (output of the wiener filter).

### References: ###
Implementations of the spectrogram and butterworth filters were referred from the following
sources:
1. spectrogram.py:
https://ursinus-cs372-s2023.github.io/Modules/Module11/Video1
2. bworth_filter.py:
https://medium.com/@ChanakaDev/low-pass-high-pass-and-band-pass-filters-with-scipy
-python-a87b2332ce25
