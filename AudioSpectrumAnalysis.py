import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from glob import glob

import librosa
import librosa.display
import IPython.display as ipd

from itertools import cycle

file, sr = librosa.load('Sound_Effects_TTL_2023-05-10,10;19;25.wav')
# print(f'y: {file[:10]}')
# print(f'shape y: {file.shape}')
# print(f'sr: {sr}')
print(librosa.get_duration(y=file, sr=sr))  # uses metadata, not actual length of wave

segmentDurationS = 20
segment_length = sr * segmentDurationS

# splice into clips isolating each frequency for testing
firstSegment = file[:segment_length]
clickSegment = file[(int(sr * 2.98)):(sr * 3)]
beepSegment = file[(int(sr * 3.5)):(int(sr * 3.52))]
voiceSegment = file[(sr * 10):(int(sr * 10.02))]


# mean frequency calculation
def find_average_frequency(signal, sr=sr):
    ft = np.fft.fft(signal)
    magnitude_spectrum = np.abs(ft)

    frequency = np.linspace(0, sr, len(magnitude_spectrum))
    num_frequency_bins = int(len(frequency) * 0.5)
    if num_frequency_bins == 0:
        num_frequency_bins = 1

    temp = 0
    for i in range(len(frequency[:num_frequency_bins])):
        temp = temp + (i * magnitude_spectrum[i])
    temp = temp / num_frequency_bins

    return frequency[int(temp)]


# print("click segment", find_average_frequency(clickSegment, sr))
# print("beep segment", find_average_frequency(beepSegment, sr))
# print("voice segment", find_average_frequency(voiceSegment, sr))

# CODE FOR PLOTTING MAGNITUDE SPECTRUM
def plot_magnitude_spectrum(signal, title, sr, f_ratio=1):
    ft = np.fft.fft(signal)
    magnitude_spectrum = np.abs(ft)

    # plot magnitude spectrum
    plt.figure(figsize=(18, 5))

    frequency = np.linspace(0, sr, len(magnitude_spectrum))
    num_frequency_bins = int(len(frequency) * f_ratio)

    plt.plot(frequency[:num_frequency_bins], magnitude_spectrum[:num_frequency_bins])
    plt.xlabel('Frequency (Hz)')
    plt.title(title)

    '''
    print(title)
    print(frequency)
    print(magnitude_spectrum)
    print("\n")
    '''

    plt.show()


# plot_magnitude_spectrum(clickSegment, "click segment", sr, 0.25)
# plot_magnitude_spectrum(beepSegment, "beep segment", sr, 0.25)
# plot_magnitude_spectrum(voiceSegment, "voice segment", sr, 0.25)

print("total length:")
print(segment_length)

averages = []
intervalStart = 0
intervalEnd = 0.1
segment_length = 200
print("AVERAGES BY S:")
for i in range(int(segment_length)):
    currentInterval = file[int(intervalStart * sr): int(intervalEnd * sr)]
    currentAverage = find_average_frequency(currentInterval, sr)
    averages.append(currentAverage)
    print(intervalStart, ", ", intervalEnd, ":  ", int(currentAverage))
    intervalStart = intervalEnd
    intervalEnd = intervalEnd + 0.1
# print(averages)



'''
CODE FOR SPECTOGRAM, SHOWS OVERALL FREQUENCY SHIFTS

FRAME_SIZE = 2048
HOP_SIZE = 512

S_file = librosa.stft(firstSegment, n_fft=FRAME_SIZE, hop_length=HOP_SIZE)
print(S_file.shape)

Y_file = np.abs(S_file) ** 2
print(Y_file.shape)

def plot_spectrogram(Y, sr, hop_length, y_axis="linear"):
    plt.figure(figsize=(25, 10))
    librosa.display.specshow(Y,
                             sr=sr,
                             hop_length=hop_length,
                             x_axis="time",
                             y_axis=y_axis)
    plt.colorbar(format="%+2.f")
    plt.show()

# plot_spectrogram(Y_file, sr, HOP_SIZE)

Y_log_scale = librosa.power_to_db(Y_file)
plot_spectrogram(Y_log_scale, sr, HOP_SIZE)

'''
