import torch
import torch.nn as nn
import torch.nn.functional as F

class CNNModel(nn.Module):
    def __init__(self, num_classes):
        super(CNNModel, self).__init__()
        
        # First Convolutional Block
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=32, kernel_size=3, stride=1, padding=1)  # (1, 128, 321) -> (32, 128, 321)
        self.pool1 = nn.MaxPool2d(kernel_size=2, stride=2, padding=0)  # (32, 128, 321) -> (32, 64, 160)
        
        # Second Convolutional Block
        self.conv2 = nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, stride=1, padding=1)  # (32, 64, 160) -> (64, 64, 160)
        self.pool2 = nn.MaxPool2d(kernel_size=2, stride=2, padding=0)  # (64, 64, 160) -> (64, 32, 80)
        
        # Third Convolutional Block
        self.conv3 = nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3, stride=1, padding=1)  # (64, 32, 80) -> (128, 32, 80)
        self.pool3 = nn.MaxPool2d(kernel_size=2, stride=2, padding=0)  # (128, 32, 80) -> (128, 16, 40)
        
        # Flatten before feeding into fully connected layers
        self.flatten = nn.Flatten()
        
        # Fully Connected Layers
        self.fc1 = nn.Linear(128 * 16 * 40, 512)  # 128 channels, 16 height, 40 width
        self.fc2 = nn.Linear(512, num_classes)  # num_classes is the number of output classes
        
    def forward(self, x):
        # Pass through convolutional layers with ReLU activations and pooling
        x = self.pool1(F.relu(self.conv1(x)))  # (1, 128, 321) -> (32, 128, 321) -> (32, 64, 160)
        x = self.pool2(F.relu(self.conv2(x)))  # (32, 64, 160) -> (64, 64, 160) -> (64, 32, 80)
        x = self.pool3(F.relu(self.conv3(x)))  # (64, 32, 80) -> (128, 32, 80) -> (128, 16, 40)
        
        # Flatten the output before passing to fully connected layers
        x = self.flatten(x)
        
        # Pass through fully connected layers
        x = F.relu(self.fc1(x))  # Fully connected layer 1
        x = self.fc2(x)  # Output layer with num_classes units
        
        return x