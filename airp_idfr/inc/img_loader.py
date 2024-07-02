import os
from PIL import Image
from torchvision import transforms
from torch.utils.data import Dataset, DataLoader

class CustomImageDataset(Dataset):
    def __init__(self, root_dir, transform=None):
        self.root_dir = root_dir
        self.transform = transform
        self.classes = os.listdir(root_dir)
        self.file_paths = []
        self.labels = []

        for label, cls in enumerate(self.classes):
            cls_dir = os.path.join(root_dir, cls)
            for file_name in os.listdir(cls_dir):
                if file_name.endswith(('.jpg', '.jpeg', '.png')):
                    self.file_paths.append(os.path.join(cls_dir, file_name))
                    self.labels.append(label)

    def __len__(self):
        return len(self.file_paths)

    def __getitem__(self, idx):
        img_path = self.file_paths[idx]
        image = Image.open(img_path).convert("RGB")
        label = self.labels[idx]

        if self.transform:
            image = self.transform(image)

        return image, label

