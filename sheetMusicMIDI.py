from music21 import converter, tempo

# Load the MusicXML file
score = converter.parse('nsynth/Someone You Loved.xml')

# Initialize a list to store notes and their timestamps
timestamps = []

# Iterate over the score to extract all actual notes (ignore chord symbols)
for element in score.flat.notes:
    if element.isNote:  # If the element is a single note
        start_time = element.offset  # Start time of the note in quarter notes
        note_name = element.nameWithOctave  # Get the full pitch name with octave (e.g., 'C4', 'D#4')
        timestamps.append((note_name, start_time))
    
    elif element.isChord:  # If the element is a chord (multiple notes played simultaneously)
        for pitch in element.pitches:
            start_time = element.offset  # Start time of the chord (same for all notes in the chord)
            note_name = pitch.nameWithOctave  # Get the full pitch name with octave (e.g., 'C4', 'A#3')
            timestamps.append((note_name, start_time))

# Sort the timestamps by time (start time of each note)
timestamps.sort(key=lambda x: x[1])

# Output the notes and their corresponding times
for note, time in timestamps:
    print(f"Note: {note}, Time: {time} quarter notes")

# Convert to seconds
bpm = None

# Loop through all elements in the score to find tempo markings (MetronomeMark)
for element in score.flat:
    if isinstance(element, tempo.MetronomeMark):
        bpm = element.getQuarterBPM() # Get tempo in BPM

# If tempo was found, print it; otherwise, print a default message
if bpm is not None:
    print(f"Tempo: {bpm} BPM")
else:
    print("No tempo marking found. Using default tempo.")
    bpm = 120  # Use a default BPM (e.g., 120) if no tempo is found

# Now bpm is the tempo in beats per minute (BPM)
