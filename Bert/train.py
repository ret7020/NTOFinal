import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision.transforms import transforms
from model import VideoQANet
from dataset import MyVideoQADataset

# Define hyperparameters
num_epochs = 10
batch_size = 32
learning_rate = 0.001

# Define data transformations
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225])
])

# Define the dataset and data loader
dataset = MyVideoQADataset(transform=transform)
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

# Instantiate the model, loss function, and optimizer
model = VideoQANet(video_feature_size=512, question_feature_size=768, num_classes=len(dataset.answers))
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=learning_rate)

# Train the model
for epoch in range(num_epochs):
    for i, batch in enumerate(dataloader):
        # Get the video frames and question tokens
        video_frames = batch['video']
        question_tokens = batch['question']

        # Get the target answers
        answers = batch['answer']

        # Forward pass
        output = model(video_frames, question_tokens)

        # Compute loss
        loss = criterion(output, answers)

        # Backward pass and optimization
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        # Print training progress
        if (i+1) % 100 == 0:
            print(f"Epoch [{epoch+1}/{num_epochs}], Step [{i+1}/{len(dataloader)}], Loss: {loss.item():.4f}")

