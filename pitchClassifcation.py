from CNNModel import CNNModel
import torch
from torch.utils.data import DataLoader
from nsynthDataset import NSynthCustom
import torchaudio
import torch.nn.functional as F
import nsynthDataset

def pitchClassification(filepath):
    # Load the model with 88 classes
    loaded_model = CNNModel(88)
    loaded_model.load_state_dict(torch.load(f="/Users/guja/Coding/NoteRecognition/models/nsynthCNNModel_5_epochs.pth"))

    # Specify device
    device = "mps"
    # Move model to mps
    loaded_model = loaded_model.to(device)

    # Put model in evaluation mode
    loaded_model.eval()
    with torch.inference_mode():
        # Transformation function for .wav file --> sample rate is 16000
        transformation = torchaudio.transforms.MelSpectrogram(16000)

        # Load the audio
        waveform, sr = torchaudio.load(filepath)

        # Resample audio if needed
        waveform = torchaudio.transforms.Resample(orig_freq=sr, new_freq=16000)(waveform)

        # Apply melspectrogram transformation to waveform
        mel_spectrogram = transformation(waveform)

        # Pad with zeros at the end of the time dimension to fit tensor input size
        mel_spectrogram = F.pad(mel_spectrogram, (0, 321 - mel_spectrogram.shape[2]))
        mel_spectrogram = mel_spectrogram.unsqueeze(0)

        # Move to mps
        mel_spectrogram = mel_spectrogram.to(device)

        # Output results
        outputs = loaded_model(mel_spectrogram)
        _, predicted = torch.max(outputs, 1)
        
        return predicted

if __name__ == "__main__":
    transformation = torchaudio.transforms.MelSpectrogram(16000)
    train_data_custom = nsynthDataset.NSynthCustom(targ_dir="/Users/guja/Coding/NoteRecognition/data/test", transform=transformation)
    print(train_data_custom.class_to_idx)

    print(pitchClassification("/Users/guja/Coding/NoteRecognition/testTest0.wav"))