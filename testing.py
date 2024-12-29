from CNNModel import CNNModel
import torch
from torch.utils.data import DataLoader
from nsynthDataset import NSynthCustom
import torchaudio

transformation = torchaudio.transforms.MelSpectrogram(sample_rate=16000)
test_data_custom = NSynthCustom(targ_dir="nsynth/data/test", transform=transformation)
test_dataloader = DataLoader(dataset=test_data_custom,
                             batch_size=32,
                             shuffle=False)

loaded_model = CNNModel(88)
loaded_model.load_state_dict(torch.load(f="nsynth/models/nsynthCNNModel_5_epochs.pth"))

device = "mps"
loaded_model = loaded_model.to(device)


loaded_model.eval()
with torch.inference_mode():
    correct = 0
    total = 0
    for inputs, labels in test_dataloader:
        inputs, labels = inputs.to(device), labels.to(device)
        outputs = loaded_model(inputs)
        _, predicted = torch.max(outputs, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

    print(f"Test Accuracy: {100 * correct / total:.2f}%")