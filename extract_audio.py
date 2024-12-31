from sheetMusicMIDI import findSeconds
from to_wav import convert_to_wav
from pydub import AudioSegment
import os

# Function to calculate appropriate start time and end time
# IMPORTANT: Under assumption multiple notes can not be played at the same time due to
# the current model. Current model can only identify single notes at this time.
def boundary_times(times, duration):
    # times is list of times in seconds; duration in milliseconds
    result = []
    for i in range(len(times)):
        # time format is (note name, start time in seconds, start time in quarter notes)
        if i == len(times) - 1:
            start_time = (times[i][1] * 1000) - 5
            end_time = duration
        else:
            if (times[i][1] * 1000) == 0.0:
                start_time = 0.0
            else:
                start_time = (times[i][1] * 1000) - 5

            end_time = (times[i + 1][1] * 1000) - 5

        result.append([start_time, end_time])

    return result
    
def extract_audio_segment(input_file, start_time_ms, end_time_ms, output_file):
    audio = AudioSegment.from_file(input_file)
    segment = audio[start_time_ms: end_time_ms]

    # Check if samplerate is 16000
    segment.export(output_file, format="wav", parameters=["-ar", "16000"])

    # TODO: Export to a folder

def extract_audio(sheet_music_filepath, audio_filepath):
    # Get filepath to sheet music and output notes and timestamps--> TODO: get input from user
    times = findSeconds(sheet_music_filepath)
    
    audio_file = audio_filepath
    # Find the duration in milliseconds
    duration = len(AudioSegment.from_file(audio_file))

    # Directory where the audio segments will be saved
    output_directory = "extracted_audio_segments"

    # Create the directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    time_intervals = boundary_times(times, duration)
    for i in range(len(time_intervals)):
        output_file = os.path.join(output_directory, f"testTest{i}.wav")
        extract_audio_segment(audio_file, time_intervals[i][0], time_intervals[i][1], output_file)

