
import numpy as np
from scipy.io import wavfile
from scipy.io.wavfile import write
from scipy.fft import fft, fftfreq, ifft
import matplotlib.pyplot as plt
from pydub import AudioSegment
import os

def amplify_sig(audio_data, amp_factor):

    audio_data_fft = fft(audio_data)
    audio_data_fft_amp = amp_factor * audio_data_fft
    audio_data_amp = ifft(audio_data_fft_amp)

    return audio_data_amp 


if __name__ == '__main__':
    input_path = 'Outputs'
    output_path = 'Outputs'
    audio_file_name = 'h_600_SubwayShort'

    if os.path.exists(input_path + '/' + audio_file_name + '.m4a'):
        audio = AudioSegment.from_file(input_path + '/' + audio_file_name + '.m4a')
        file_handle = audio.export(input_path + '/' + audio_file_name + '.wav', format='wav')
    samplerate, data = wavfile.read(input_path + '/' + audio_file_name + '.wav')
    if len(list(data.shape))==2:
        data = data[:,0]

    amp_factor = 3
    data_amp = amplify_sig(data, amp_factor)

    write(output_path + '/' + audio_file_name+ '_amp_' + str(amp_factor) +'.m4a',samplerate,data_amp.astype(np.int16))

    # Plot the original and filtered data
    plt.figure(figsize=(10, 6))
    plt.plot([t for t in range(len(list(data)))], data_amp, 'b', label='Amplified Signal')
    plt.plot([t for t in range(len(list(data)))], data, 'r', label='Original Signal')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Audio Amplification Example')
    plt.legend()
    plt.grid(True)
    plt.show()