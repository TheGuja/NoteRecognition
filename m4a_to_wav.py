from pydub import AudioSegment

def convert_m4a_to_wav(input_file, output_file, target_sample_rate=None):
    audio = AudioSegment.from_file(input_file, format="m4a")

    if target_sample_rate:
        audio = audio.set_frame_rate(target_sample_rate)

    audio.export(output_file, format="wav")


# input_m4a = "nsynth/New Recording 9.m4a"
# output_wav = "nsynth/C.wav"
# target_sample_rate = 16000

# convert_m4a_to_wav(input_m4a, output_wav, target_sample_rate)