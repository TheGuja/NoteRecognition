import numpy as np
from pydub import AudioSegment
import os

# Function to add noise to a single .wav file
def add_noise_to_wav(input_file, output_file, noise_level):
    # Load the .wav file
    audio = AudioSegment.from_wav(input_file)

    # Convert audio to numpy array
    samples = np.array(audio.get_array_of_samples())

    # Generate random noise (Gaussian noise)
    noise = np.random.normal(0, noise_level * np.max(np.abs(samples)), len(samples))

    # Add the noise to the original samples
    noisy_samples = samples + noise.astype(np.int16)

    # Ensure the result is within the acceptable range for audio samples
    noisy_samples = np.clip(noisy_samples, -32768, 32767)

    # Convert back to AudioSegment
    noisy_audio = audio._spawn(noisy_samples.tobytes())
    noisy_audio = noisy_audio.set_frame_rate(audio.frame_rate)

    # Export noisy audio
    noisy_audio.export(output_file, format="wav")



if __name__ == "__main__":

    parent_dir = "/Users/guja/Coding/NoteRecognition/data/train"
    for folder in os.listdir(parent_dir):
        if (folder != '.DS_Store'):
            input_folder = os.path.join(parent_dir, folder)
            output_folder = input_folder

            # Loop over all .wav files in the input folder and apply noise
            for filename in os.listdir(input_folder):
                if filename.endswith(".wav"):
                    input_file = os.path.join(input_folder, filename)
                    output_file1 = os.path.join(output_folder, f"noisy_{filename}_0.1")
                    output_file2 = os.path.join(output_folder, f"noisy_{filename}_0.2")
                    
                    add_noise_to_wav(input_file, output_file1, 0.1)
                    add_noise_to_wav(input_file, output_file2, 0.2)

    
    print("All files processed.")