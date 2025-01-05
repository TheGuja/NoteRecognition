import torch
import torch.nn as nn
import torch.nn.functional as F

class CNNModel(nn.Module):
    def __init__(self, num_classes, dropout_prob=0.05):
        super(CNNModel, self).__init__()
        
        # First Convolutional Block
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=32, kernel_size=3, stride=1, padding=1)  # (1, 128, 321) -> (32, 128, 321)
        self.pool1 = nn.MaxPool2d(kernel_size=2, stride=2, padding=0)  # (32, 128, 321) -> (32, 64, 160)
        self.dropout1 = nn.Dropout2d(dropout_prob)  # Dropout layer after conv1

        # Second Convolutional Block
        self.conv2 = nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, stride=1, padding=1)  # (32, 64, 160) -> (64, 64, 160)
        self.pool2 = nn.MaxPool2d(kernel_size=2, stride=2, padding=0)  # (64, 64, 160) -> (64, 32, 80)
        self.dropout2 = nn.Dropout2d(dropout_prob)  # Dropout layer after conv2
        
        # Third Convolutional Block
        self.conv3 = nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3, stride=1, padding=1)  # (64, 32, 80) -> (128, 32, 80)
        self.pool3 = nn.MaxPool2d(kernel_size=2, stride=2, padding=0)  # (128, 32, 80) -> (128, 16, 40)
        self.dropout3 = nn.Dropout2d(dropout_prob)  # Dropout layer after conv3
        
        # Fourth Convolutional Block
        self.conv4 = nn.Conv2d(in_channels=128, out_channels=256, kernel_size=3, stride=1, padding=1) # (128, 16, 40) -> (256, 16, 40)
        self.pool4 = nn.MaxPool2d(kernel_size=2, stride=2) # (256, 16, 40) -> (256, 8, 20)
        self.dropout4 = nn.Dropout2d(dropout_prob)  # Dropout layer after conv4
        
        # Flatten before feeding into fully connected layers
        self.flatten = nn.Flatten()
        
        # Fully Connected Layers
        self.fc1 = nn.Linear(256 * 8 * 20, 512)  # 256 channels, 8 height, 20 width
        self.fc2 = nn.Linear(512, num_classes)  # num_classes is the number of output classes
        self.dropout_fc = nn.Dropout(dropout_prob)  # Dropout layer for fully connected layer

    def forward(self, x):
        # Pass through convolutional layers with ReLU activations and pooling
        x = self.pool1(F.relu(self.conv1(x)))  # (1, 128, 321) -> (32, 128, 321) -> (32, 64, 160)
        x = self.dropout1(x)  # Apply dropout after conv1
        
        x = self.pool2(F.relu(self.conv2(x)))  # (32, 64, 160) -> (64, 64, 160) -> (64, 32, 80)
        x = self.dropout2(x)  # Apply dropout after conv2
        
        x = self.pool3(F.relu(self.conv3(x)))  # (64, 32, 80) -> (128, 32, 80) -> (128, 16, 40)
        x = self.dropout3(x)  # Apply dropout after conv3
        
        x = self.pool4(F.relu(self.conv4(x)))  # (128, 16, 40) -> (256, 16, 40) -> (256, 8, 20)
        x = self.dropout4(x)  # Apply dropout after conv4
        
        # Flatten the output before passing to fully connected layers
        x = self.flatten(x)
        
        # Pass through fully connected layers with dropout
        x = F.relu(self.fc1(x))  # Fully connected layer 1
        x = self.dropout_fc(x)  # Apply dropout after fc1
        x = self.fc2(x)  # Output layer with num_classes units
        
        return x
