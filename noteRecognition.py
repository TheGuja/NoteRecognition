from  sheetMusicMIDI import findSeconds
import sounddevice as sd
import sys
import time
import numpy as np
import threading

# Get filepath --> TODO: get input from user
filepath = "/Users/guja/Coding/NoteRecognition/Someone You Loved.xml"

# Output notes and seconds
tempo, times = findSeconds(filepath)

# TODO: Implement a starting time indicator --> maybe something like give two bars of tempo and start recording after
# That's a bad idea --> maybe just wait for two bars of time and console.log the beats?
sr = 16000
time.sleep(8 * tempo)

# Flag to control when to stop recording
recording_active = True

# List to store the recorded audio chunks
recorded_audio = []

# Callback function to capture audio data
def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    recorded_audio.append(indata.copy())

# Function to monitor user input in a separate thread
def monitor_input():
    global recording_active
    input("Press Enter to stop recording...\n")
    recording_active = False  # Stop the recording when Enter is pressed

# Function to start recording
def record_until_input():
    global recorded_audio, recording_active

    print("Recording started. Press Enter to stop.")
    
    # Start the input monitoring in a separate thread
    input_thread = threading.Thread(target=monitor_input)
    input_thread.daemon = True  # Allow the thread to be terminated when the program ends
    input_thread.start()

    # Start the recording stream
    with sd.InputStream(callback=callback, channels=1, samplerate=sr):
        while recording_active:
            time.sleep(0.1)  # Sleep to avoid maxing out the CPU

    # Concatenate all recorded chunks into a single numpy array
    audio_data = np.concatenate(recorded_audio, axis=0)
    return audio_data

# Start recording
audio_data = record_until_input()

# Use notes and seconds information to record at specific points in time

