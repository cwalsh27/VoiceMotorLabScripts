import wave
import os
import glob

def split_wav_with_labels(input_file, output_dir, labels, times, initials, run_number, prepost):
    """
    Split a .wav file according to given labels and start-times.

    Parameters:
        input_file (str): Path to the input wav file.
        output_dir (str): Directory to save the chunks.
        labels (list): List of labels for each segment.
        times (list): List of start times (in seconds) for each segment.
                      The last segment will run until EOF.
    """
    os.makedirs(output_dir, exist_ok=True)

    with wave.open(input_file, 'rb') as wav:
        frame_rate = wav.getframerate()
        n_channels = wav.getnchannels()
        samp_width = wav.getsampwidth()
        total_frames = wav.getnframes()

        # Convert start times to frame positions
        start_frames = [int(t * frame_rate) for t in times]
        start_frames.append(total_frames)  # add end-of-file marker

        for i, label in enumerate(labels):
            start_frame = start_frames[i]
            end_frame = start_frames[i + 1]
            num_frames = end_frame - start_frame

            wav.setpos(start_frame)
            frames = wav.readframes(num_frames)

            output_file = os.path.join(output_dir, f"{initials}_run{run_number}_{prepost}_{i:03d}_{label}.wav")

            with wave.open(output_file, 'wb') as out_wav:
                out_wav.setnchannels(n_channels)
                out_wav.setsampwidth(samp_width)
                out_wav.setframerate(frame_rate)
                out_wav.writeframes(frames)

            print(f"Saved {output_file}")


if __name__ == "__main__":

    labels146 = [
        "sing","cue-sing","sing","cue-sing","sing","Fixation1","Fixation1","cue-nosing",
        "nosing","cue-nosing","nosing","cue-nosing","nosing","Fixation2","Fixation2",
        "cue-sing","sing","cue-sing","sing","cue-sing","sing","Fixation1","Fixation1",
        "cue-nosing","nosing","cue-nosing","nosing","cue-nosing","nosing","Fixation2",
        "Fixation2","cue-sing","sing","cue-sing","sing","cue-sing","sing","Fixation1",
        "Fixation1","cue-nosing","nosing","cue-nosing","nosing","cue-nosing","nosing",
        "Fixation2","Fixation2","cue-sing","sing","cue-sing","sing","cue-sing","sing",
        "Fixation1","Fixation1","cue-nosing","nosing","cue-nosing","nosing","cue-nosing",
        "nosing","Fixation2","Fixation2","Fixation2"
    ]

    times146 = [
        8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60,
        64, 68, 72, 76, 80, 84, 88, 92, 96,100,104,108,112,116,120,
        124,128,132,136,140,144,148,152,156,160,164,168,172,176,180,
        184,188,192,196,200,204,208,212,216,220,224,228,232,236,240,
        244,248,252,256,260
    ]

    labels235 = [
        "nosing","cue-nosing","nosing","cue-nosing","nosing","Fixation1","Fixation1","cue-sing",
        "sing","cue-sing","sing","cue-sing","sing","Fixation2","Fixation2",
        "cue-nosing","nosing","cue-nosing","nosing","cue-nosing","nosing","Fixation1","Fixation1",
        "cue-sing","sing","cue-sing","sing","cue-sing","sing","Fixation2",
        "Fixation2","cue-nosing","nosing","cue-nosing","nosing","cue-nosing","nosing","Fixation1",
        "Fixation1","cue-sing","sing","cue-sing","sing","cue-sing","sing",
        "Fixation2","Fixation2","cue-nosing","nosing","cue-nosing","nosing","cue-nosing","nosing",
        "Fixation1","Fixation1","cue-sing","sing","cue-sing","sing","cue-sing",
        "sing","Fixation2","Fixation2","Fixation2"
    ]

    times235 = [
        8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60,
        64, 68, 72, 76, 80, 84, 88, 92, 96,100,104,108,112,116,120,
        124,128,132,136,140,144,148,152,156,160,164,168,172,176,180,
        184,188,192,196,200,204,208,212,216,220,224,228,232,236,240,
        244,248,252,256,260
    ]

    directory_input = input("Enter the full directory of the folder with your .wav files.")
    files = glob.glob(directory_input + "/*/*.wav", recursive=True)
    output_dir = "labeled_splices"

    

    for file in files:
        if "labeled_splices" in file:
            continue

        subject_initials = file.split("/")[-1].split("_")[0]

        run_number = file.lower().split("run")[-1][0]

        prepost_letter = file.split("_")[-1].split(".wav")[0]


        if "run1" in file.lower() or "run4" in file.lower() or "run6" in file.lower():
            split_wav_with_labels(file, output_dir, labels146, times146, subject_initials, run_number, prepost_letter)
        elif "run2" in file.lower() or "run3" in file.lower() or "run5" in file.lower():
            split_wav_with_labels(file, output_dir, labels235, times235, subject_initials, run_number, prepost_letter)
        else:
            print(f"Run not recognized in {file}. Confirm that 'runx' is included in the file name denoting the run number. (i.e., 'run2')")
            


    



    
