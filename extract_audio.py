from sheetMusicMIDI import findSeconds
from to_wav import convert_to_wav
from pydub import AudioSegment

# Function to calculate appropriate start time and end time
# IMPORTANT: Under assumption multiple notes can not be played at the same time due to
# the current model. Current model can only identify single notes at this time.
def boundary_times(times, duration):
    # times is list of times in seconds; duration in milliseconds
    result = []
    for i in range(len(times) - 1):
        # time format is (note name, start time in seconds, start time in quarter notes)
        if len(times - 1):
            start_time = (times[i][1] * 1000) - 100
            end_time = duration
        else:
            if times[i][1] == 0:
                start_time = 0
            else:
                start_time = times[i][1] - 100

            end_time = times[i + 1][1] - 100

        result.append([start_time, end_time])

    return result
    
def extract_audio_segment(input_file, start_time_ms, end_time_ms, output_file):
    audio = AudioSegment.from_file(input_file)
    segment = audio[start_time_ms: end_time_ms]

    segment.export(output_file, format="wav")

    # TODO: Export to a folder

def extract_audio(sheet_music_filepath, audio_filepath):
    # Get filepath to sheet music and output notes and timestamps--> TODO: get input from user
    # sheet_music_filepath = "/Users/guja/Coding/NoteRecognition/Someone You Loved.xml"
    times = findSeconds(sheet_music_filepath)
    
    audio_file = audio_filepath
    # Find the duration in milliseconds
    duration = len(AudioSegment.from_file(audio_file))

    time_intervals = boundary_times(times, duration)
    for intervals in time_intervals:
        extract_audio_segment(audio_file, intervals[0], intervals[1])



