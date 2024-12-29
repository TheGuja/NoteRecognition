import os

folder_path = "nsynth/data/train/A0"

# Loop through all files in the directory
count = 0
for filename in os.listdir(folder_path):
    # Check if the file is a .wav file
    if filename.endswith(".wav"):
        # If the filename contains "keyboard", skip it
        if "keyboard" in filename:
            # file_path = os.path.join(folder_path, filename)
            # waveform, sr = torchaudio.load(file_path)
            # print(sr)
            count += 1
        # Otherwise, remove the file
        else:
            file_path = os.path.join(folder_path, filename)
            os.remove(file_path)
            print(f"Removed: {filename}")