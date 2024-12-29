from music21 import converter, tempo

def findSeconds(filepath):
    # Load XML, MIDI file
    score = converter.parse(filepath)

    bpm = None
    # Loop through all elements in the score to find tempo markings (MetronomeMark)
    for element in score.flatten():
        if isinstance(element, tempo.MetronomeMark):
            bpm = element.getQuarterBPM() # Get tempo in BPM

    # Use default BPM if no tempo is found
    if bpm is None:
        bpm = 120

    beats_per_second = 60 / bpm

    # Initialize a list to store notes and their timestamps
    timestamps = []

    # Iterate over the score to extract all actual notes (ignore chord symbols)
    for element in score.flatten().notes:
        if element.isNote:  # If the element is a single note
            start_time = element.offset  # Start time of the note in quarter notes
            note_name = element.nameWithOctave  # Get the full pitch name with octave (e.g., 'C4', 'D#4')
            timestamps.append((note_name, start_time * beats_per_second, start_time))
        
        elif element.isChord:  # If the element is a chord (multiple notes played simultaneously)
            for pitch in element.pitches:
                start_time = element.offset  # Start time of the chord (same for all notes in the chord)
                note_name = pitch.nameWithOctave  # Get the full pitch name with octave (e.g., 'C4', 'A#3')
                timestamps.append((note_name, start_time * beats_per_second, start_time))

    # Sort the timestamps by time (start time of each note)
    timestamps.sort(key=lambda x: x[1])

    # Output the notes and their corresponding times
    return bpm, timestamps

print(findSeconds("/Users/guja/Coding/NoteRecognition/Someone You Loved.xml"))