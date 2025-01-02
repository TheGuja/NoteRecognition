from pitchClassifcation import pitchClassification
import os

classes = {'A#0': 0, 'A#1': 1, 'A#2': 2, 'A#3': 3, 'A#4': 4, 'A#5': 5, 'A#6': 6, 'A#7': 7, 'A0': 8, 'A1': 9, 'A2': 10, 'A3': 11, 'A4': 12, 'A5': 13, 'A6': 14, 'A7': 15, 'B0': 16, 'B1': 17, 'B2': 18, 'B3': 19, 'B4': 20, 'B5': 21, 'B6': 22, 'B7': 23, 'C#1': 24, 'C#2': 25, 'C#3': 26, 'C#4': 27, 'C#5': 28, 'C#6': 29, 'C#7': 30, 'C1': 31, 'C2': 32, 'C3': 33, 'C4': 34, 'C5': 35, 'C6': 36, 'C7': 37, 'C8': 38, 'D#1': 39, 'D#2': 40, 'D#3': 41, 'D#4': 42, 'D#5': 43, 'D#6': 44, 'D#7': 45, 'D1': 46, 'D2': 47, 'D3': 48, 'D4': 49, 'D5': 50, 'D6': 51, 'D7': 52, 'E1': 53, 'E2': 54, 'E3': 55, 'E4': 56, 'E5': 57, 'E6': 58, 'E7': 59, 'F#1': 60, 'F#2': 61, 'F#3': 62, 'F#4': 63, 'F#5': 64, 'F#6': 65, 'F#7': 66, 'F1': 67, 'F2': 68, 'F3': 69, 'F4': 70, 'F5': 71, 'F6': 72, 'F7': 73, 'G#1': 74, 'G#2': 75, 'G#3': 76, 'G#4': 77, 'G#5': 78, 'G#6': 79, 'G#7': 80, 'G1': 81, 'G2': 82, 'G3': 83, 'G4': 84, 'G5': 85, 'G6': 86, 'G7': 87}
print(classes)
# output_directory = "/Users/guja/Coding/NoteRecognition/extracted_audio_segments"

# Get a list of all files in the directory and filter for .wav files
wav_files = [f for f in os.listdir("/Users/guja/Coding/NoteRecognition/extracted_audio_segments") if f.endswith(".wav")]

# Sort the files numerically by extracting the integer from the filename
wav_files.sort(key=lambda x: int(x.replace('testTest', '').replace('.wav', '')))

# Loop through the sorted files
for filename in wav_files:
    # Get the full file path
    file_path = os.path.join("/Users/guja/Coding/NoteRecognition/extracted_audio_segments", filename)
    print(pitchClassification(file_path))