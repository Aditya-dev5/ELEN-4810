import numpy as np
from scipy.signal import butter, filtfilt
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.io.wavfile import write
from scipy.fft import fft, fftfreq, ifft
import matplotlib.pyplot as plt
from pydub import AudioSegment
from scipy.signal import stft
import os

def get_filter(type, cutoff, order, samplerate):
    cutoff_low = cutoff[0]
    cutoff_high = cutoff[1]

    fs = samplerate  # Sampling rate in Hz

    # Design the filter
    nyq = 0.5 * fs
    nyq_cutoff_low = cutoff_low / nyq
    nyq_cutoff_high = cutoff_high / nyq
    nyq_cutoff = (nyq_cutoff_low,nyq_cutoff_high)

    if type == 'highpass':
        nyq_cutoff_freq = nyq_cutoff[0]
    elif type == 'lowpass':
        nyq_cutoff_freq = nyq_cutoff[1]
    elif type == 'bandpass':
        nyq_cutoff_freq = nyq_cutoff

    b, a = butter(order, nyq_cutoff_freq, btype=type)

    return b,a


if __name__ == '__main__':
    input_path = 'Data'
    output_path = 'Outputs'
    audio_file_name = 'SubwayShort'
    output_figures = 'Figures'

    if os.path.exists(input_path + '/' + audio_file_name + '.m4a'):
        audio = AudioSegment.from_file(input_path + '/' + audio_file_name + '.m4a')
        file_handle = audio.export(input_path + '/' + audio_file_name + '.wav', format='wav')
    samplerate, data = wavfile.read(input_path + '/' + audio_file_name + '.wav')
    if len(list(data.shape))==2:
        data = data[:,0]

    low = 600
    high = 20000
    cutoff = (low,high)
    order = 4
    type = 'highpass'
    b,a = get_filter(type, cutoff, order, samplerate)

    # Apply the filter
    filtered_data = filtfilt(b, a, data)
    if type == 'highpass':
        write(output_path + '/' + str(type[0])+'_'+str(low)+'_' + audio_file_name+ '.m4a',samplerate,filtered_data.astype(np.int16))
    if type == 'lowpass':
        write(output_path + '/' + str(type[0])+'_'+str(high)+'_' + audio_file_name+ '.m4a',samplerate,filtered_data.astype(np.int16))
    if type == 'bandpass':
        write(output_path + '/' + str(type[0])+'_'+str(low)+'_'+str(high) + audio_file_name+ '.m4a',samplerate,filtered_data.astype(np.int16))

    # Plot the original and filtered data
    plt.figure(figsize=(10, 6))
    plt.plot([t for t in range(len(list(data)))], data, label='Original Signal')
    plt.plot([t for t in range(len(list(data)))], filtered_data, label='Filtered Signal')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Output of %s-filter'%(type))
    plt.legend()
    plt.grid(True)
    plt.savefig(output_path+'/'+output_figures+'/'+audio_file_name+'_filtered.jpg')
    plt.show()
        
