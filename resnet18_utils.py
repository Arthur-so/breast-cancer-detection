import torch
from torchvision import transforms
import torch.backends.cudnn as cudnn
from torch.utils.data import Dataset, DataLoader

from PIL import Image
import os

# Clear cuda cache before starting:
torch.cuda.empty_cache()
cudnn.benchmark = True

class CustomImageDataset(Dataset):
    def __init__(self, images_list, root_path, transform=None):
        self.images_list = images_list
        self.transform = transform
        self.root_path = root_path

    def __len__(self):
        return len(self.images_list)

    def __getitem__(self, idx):
        img_name = os.path.join(self.root_path, self.images_list[idx]['subfolder'], self.images_list[idx]['img'])
        image = Image.open(img_name).convert('RGB')
        label = self.images_list[idx]['label']

        if self.transform:
            image = self.transform(image)

        return image, label

def resnet18_data_preprocessing(images_list, root_path, batch_size=32, workers=2, device='cuda:0'):
    # Define the standard size for ResNet18
    RESNET18_RESIZE = 100
    RESNET_NORMALIZE_VALUES = ([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])

    # Compose data transformations:
    data_transforms = transforms.Compose([
        transforms.Resize((RESNET18_RESIZE, RESNET18_RESIZE)),
        transforms.ToTensor(),
        transforms.Normalize(*RESNET_NORMALIZE_VALUES)
    ])

    # Create datasets
    train_dataset = CustomImageDataset(images_list[0], root_path, transform=data_transforms)
    test_dataset = CustomImageDataset(images_list[1], root_path, transform=data_transforms)

    # Create dataloaders
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True, num_workers=workers)
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False, num_workers=workers)

    # Dataset sizes and class names
    dataset_sizes = {'train': len(train_dataset), 'test': len(test_dataset)}
    class_names = list(set(img['label'] for img in images_list[0] + images_list[1]))

    # Config device
    device = torch.device(device if torch.cuda.is_available() else "cpu")

    return {'train': train_loader, 'test': test_loader}, dataset_sizes, class_names, device

