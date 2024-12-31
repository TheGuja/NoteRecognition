from pydub import AudioSegment

def convert_to_wav(input_file, output_file, target_sample_rate=16000):
    audio = AudioSegment.from_file(input_file)

    if target_sample_rate:
        audio = audio.set_frame_rate(target_sample_rate)

    audio.export(output_file, format="wav")