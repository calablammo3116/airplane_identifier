import time
import torch
import torch.nn as nn
import torch.nn.functional as F

class ConvNet(nn.Module):
  def __init__(self, mode):
    super(ConvNet, self).__init__()

    # Define various layers here, such as in the tutorial example
    # Convolutional layers for question 1...
    self.conv2d1_1 = nn.Conv2d(in_channels=3, out_channels=10, kernel_size=3)
    self.conv2d2_1 = nn.Conv2d(in_channels=10, out_channels=10, kernel_size=3)

    # Convolutional layers for question 2...
    self.conv2d1_2 = nn.Conv2d(in_channels=3, out_channels=20, kernel_size=3)
    self.conv2d2_2 = nn.Conv2d(in_channels=20, out_channels=40, kernel_size=3)

    self.fc1_model1 = nn.Linear(360, 100)  # This is first fully connected layer for step 1.
    self.fc1_model2 = nn.Linear(1440, 100) # This is first fully connected layer for step 2.

    self.fc2 = nn.Linear(100, 10)       # This is 2nd fully connected layer for all models.


    # This will select the forward pass function based on mode for the ConvNet.
    # Based on the question, you have 3 modes available for step 1 to 3.
    # During creation of each ConvNet model, you will assign one of the valid mode.
    # This will fix the forward function (and the network graph) for the entire training/testing
    if mode == 1:
        self.forward = self.model_1
    elif mode == 2:
        self.forward = self.model_2
    elif mode == 0:
        self.forward = self.model_0
    else:
        print("Invalid mode ", mode, "selected. Select between 0-2")
        exit(0)


  # Example model. Modify this for step 1-3
  def model_0(self, inp):
    inp = self.conv2d1_1(inp)
    inp = F.relu(inp)
    inp = F.max_pool2d(inp, kernel_size=2)
    inp = self.conv2d2_1(inp)
    inp = F.relu(inp)
    inp = F.max_pool2d(inp, kernel_size=2)

    # End of Conv-Pooling layers; begin FC layers...
    inp = torch.flatten(inp, start_dim=1)
    inp = F.relu(self.fc1_model1(inp))
    inp = self.fc2(inp)

    return inp


  # Simple CNN. step 1
  def model_1(self, inp):
    inp = self.conv2d1_1(inp)
    inp = F.relu(inp)
    inp = F.max_pool2d(inp, kernel_size=2)
    inp = self.conv2d2_1(inp)
    inp = F.relu(inp)
    inp = F.max_pool2d(inp, kernel_size=2)

    # End of Conv-Pooling layers; begin FC layers...
    inp = torch.flatten(inp, start_dim=1)
    inp = self.fc1_model1(inp)
    inp = F.relu(inp)
    inp = self.fc2(inp)

    return inp


  # Increase filters. step 2
  def model_2(self, inp):
    inp = self.conv2d1_2(inp)
    inp = F.relu(inp)
    inp = F.max_pool2d(inp, kernel_size=2)
    inp = self.conv2d2_2(inp)
    inp = F.relu(inp)
    inp = F.max_pool2d(inp, kernel_size=2)

    # End of Conv-Pooling layers; begin FC layers...
    inp = torch.flatten(inp, start_dim=1)
    inp = self.fc1_model2(inp)
    inp = F.relu(inp)
    inp = self.fc2(inp)

    return inp
