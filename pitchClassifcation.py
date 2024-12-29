from CNNModel import CNNModel
import torch
from torch.utils.data import DataLoader
from nsynthDataset import NSynthCustom
import torchaudio
import torch.nn.functional as F
import nsynthDataset

loaded_model = CNNModel(88)
loaded_model.load_state_dict(torch.load(f="nsynth/models/nsynthCNNModel_5_epochs.pth"))

device = "mps"
loaded_model = loaded_model.to(device)

# loaded_model.eval()
# with torch.inference_mode(): 
#     transformation = torchaudio.transforms.MelSpectrogram(16000, n_fft=800)
#     filepath = "nsynth/C.wav"
#     waveform, sr = torchaudio.load(filepath)
#     waveform = torchaudio.transforms.Resample(orig_freq=sr, new_freq=16000)(waveform)
#     mel_spectrogram = transformation(waveform)
#     mel_spectrogram = F.pad(mel_spectrogram, (0, 159))  # Pad with zeros at the end of the time dimension
#     mel_spectrogram = mel_spectrogram.unsqueeze(0)
#     mel_spectrogram = mel_spectrogram.to(device)
#     outputs = loaded_model(mel_spectrogram)
#     _, predicted = torch.max(outputs, 1)
#     print(predicted)

# train_data_custom = nsynthDataset.NSynthCustom(targ_dir="nsynth/data/train", transform=transformation)
# print(train_data_custom.class_to_idx)