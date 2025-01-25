from scipy.signal import wiener
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

def apply_wiener_filt(input_signal, filter_size):

    input_signal = input_signal.astype(np.float64)
    temp = input_signal / np.max(np.abs(input_signal))
    filtered_signal = wiener(input_signal,mysize=filter_size)
    return filtered_signal


if __name__ == '__main__':
    input_path = 'Outputs'
    output_path = 'Outputs'
    audio_file_name = 'h_600_SubwayShort'
    output_figures = 'Figures'

    if os.path.exists(input_path + '/' + audio_file_name + '.m4a'):
        audio = AudioSegment.from_file(input_path + '/' + audio_file_name + '.m4a')
        file_handle = audio.export(input_path + '/' + audio_file_name + '.wav', format='wav')
    samplerate, data = wavfile.read(input_path + '/' + audio_file_name + '.wav')
    if len(list(data.shape))==2:
        data = data[:,0]

    filter_size = 11
    filtered_data = apply_wiener_filt(data, filter_size)
    write(output_path + '/' + 'wiener' + '_' + str(filter_size) + '_' + audio_file_name+ '.m4a',samplerate,filtered_data.astype(np.int16))

    # Plot the original and filtered data
    plt.figure(figsize=(10, 6))
    plt.plot([t for t in range(len(list(data)))], data, label='Original Signal')
    plt.plot([t for t in range(len(list(data)))], filtered_data, label='Filtered Signal')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Output of wiener filter (size = %s)'%(filter_size))
    plt.legend()
    plt.grid(True)
    plt.savefig(output_path+'/'+output_figures+'/'+audio_file_name+'_weiner_'+str(filter_size)+'.jpg')
    plt.show()
        
