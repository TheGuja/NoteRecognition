import os
import pathlib
import torch

from torch.utils.data import Dataset
import torchaudio

def find_classes(directory):
    classes = sorted(entry.name for entry in os.scandir(directory) if entry.is_dir())

    if not classes:
        raise FileNotFoundError(f"Couldn't find any classes in {directory}.")
    
    class_to_idx = {cls_name: i for i, cls_name in enumerate(classes)}
    return classes, class_to_idx


class NSynthCustom(Dataset):
    def __init__(self, targ_dir, transform=None):
        self.paths = list(pathlib.Path(targ_dir).glob("*/*.wav"))
        self.transform = transform
        self.classes, self.class_to_idx = find_classes(targ_dir)

    def load_audio(self, index):
        audio_path = self.paths[index]
        waveform, sample_rate = torchaudio.load(audio_path)
        return waveform, sample_rate


    def __len__(self):
        return len(self.paths)
    
    def __getitem__(self, index):
        waveform, samplerate = self.load_audio(index)
        class_name = self.paths[index].parent.name
        class_idx = self.class_to_idx[class_name]

        if self.transform:
            return self.transform(waveform), class_idx
        else:
            return waveform, class_idx