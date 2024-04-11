import matplotlib.pyplot as plt
import numpy as np
import os

import librosa
import soundfile as sf

# defines path to desktop files
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
audio_dir = os.path.join(desktop_path, 'AudioFiles')
out_dir = os.path.join(desktop_path, "timeSplits/20")

audio_file = os.path.join(audio_dir, 'NR_DSP_OUT_2023-05-09,10_14_20.wav')

file, sr = librosa.load(audio_file)


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


# PLOTTING MAGNITUDE SPECTRUM (not used in current script)
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

    plt.show()


averages = []
intervalStart = 0
intervalEnd = 0.01
segment_length = 3500
print("AVERAGES BY S:")
for i in range(int(segment_length)):
    currentInterval = file[int(intervalStart * sr): int(intervalEnd * sr)]
    currentAverage = find_average_frequency(currentInterval, sr)
    averages.append(currentAverage)
    print(intervalStart, ", ", intervalEnd, ":  ", int(currentAverage))
    intervalStart = intervalEnd
    intervalEnd = intervalEnd + 0.01


# Code for identifying golden point (start of the first glide vocal exercise, aka trial 3)
goldenPoint = 0
for i in range(2800, 3200):
    currentAverage = averages[i]
    if averages[i] <= 100:
        if (averages[i-1] <= 100) and (averages[i+1] <= 100) and (averages[i+2] <= 100) and (averages[i+3] <= 100):
            goldenPoint = i / 100 - 0.01
            break

approvedGolden = input(f"The start point is {goldenPoint}. Is this correct? (Y/N)")

# CODE FOR SPLITTING INTO INTERVALS; only when golden point is correct
if(approvedGolden.lower()=="y"):
    newSegLength = 4
    newSegments = []
    # e=EE/high vowels, o = AH/back vowels, g = glide, r = rest
    intervalOrder = "groegrgeorgoereogrgeorgoerogergeorogeregoreogroegrogeroegrogergoergeoreogr"
    print(len(intervalOrder))


    for i in range(148):   # 148 number is number of remaining trials doubled, for two four second intervals per trial
        t = file[int(sr * (goldenPoint + (i * newSegLength))): int(sr * (goldenPoint + ((i + 1) * newSegLength)))]
        newSegments.append(t)

# calculates type of vocal exercise and stores in vType to be appended to the file name
    vType = ""
    for i in range(74):
        match intervalOrder[i]:
            case "e":
                vType = "highv"
            case "o":
                vType = "backv"
            case "g":
                vType = "glide"
            case "r":
                vType = "rest"
# assembles new file name from old file name, with segment/trial number and vType
        recording_name = os.path.basename(audio_file[:-4])
        out_file = f"{recording_name}_T{str(i+3)}_{vType}.wav"
        print(out_file)
        if vType != "rest":
            sf.write(os.path.join(out_dir, out_file), newSegments[i*2], int(sr))
