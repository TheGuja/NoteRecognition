import nsynthDataset
import CNNModel
import torchaudio
from torch.utils.data import DataLoader
from torch import nn
import torch
import torch.optim as optim
from tqdm import tqdm
from pathlib import Path

transformation = torchaudio.transforms.MelSpectrogram(sample_rate=16000)

train_data_custom = nsynthDataset.NSynthCustom(targ_dir="/Users/guja/Coding/NoteRecognition/data/train", transform=transformation)

train_dataloader = DataLoader(dataset=train_data_custom,
                              batch_size=32,
                              shuffle=True)


# Example usage
num_classes = 88  # Example for a classification task with 10 classes
model = CNNModel.CNNModel(num_classes)

device = "mps"
model = model.to(device)
# Loss and optimizer
criterion = nn.CrossEntropyLoss()  # For multi-class classification
optimizer = optim.Adam(model.parameters(), lr=0.001)

epochs = 10
for epoch in range(epochs):
    model.train()
    running_loss = 0.0
    correct = 0
    total = 0
    for inputs, labels in tqdm(train_dataloader):
        inputs, labels = inputs.to(device), labels.to(device)
        
        # Zero the parameter gradients
        optimizer.zero_grad()
        
        # Forward pass
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        
        # Backward pass and optimization
        loss.backward()
        optimizer.step()
        
        running_loss += loss.item()
        
        # Calculate accuracy
        _, predicted = torch.max(outputs, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

    print(f"Epoch [{epoch+1}/{epochs}], Loss: {running_loss/len(train_dataloader):.4f}, Accuracy: {100 * correct / total:.2f}%")

# 1. Create models directory 
MODEL_PATH = Path("/Users/guja/Coding/NoteRecognition/models")
MODEL_PATH.mkdir(parents=True, exist_ok=True)

# 2. Create model save path 
MODEL_NAME = "nsynthCNNModel_10_epochs.pth"
MODEL_SAVE_PATH = MODEL_PATH / MODEL_NAME

# 3. Save the model state dict 
print(f"Saving model to: {MODEL_SAVE_PATH}")
torch.save(obj=model.state_dict(), f=MODEL_SAVE_PATH)


