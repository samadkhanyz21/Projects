import os
import cv2
import torch
from torchvision.transforms import v2
from torch.utils.data import Dataset, DataLoader

# Path to dataset directory
org_data = os.environ.get('path_to_dataset', './data')

# Check if the specified path exists
if not os.path.exists(org_data):
    raise FileNotFoundError(f"The specified path '{org_data}' does not exist.")

# Check if the subdirectories exist within 'train', 'test', and 'val'
sub_dirs = ['images', 'labels']

for data_split in ['train', 'valid', 'test']:
    for sub_dir in sub_dirs:
        subdir_path = os.path.join(org_data, data_split, sub_dir)
        if not os.path.exists(subdir_path):
            print(f"Subdirectory '{sub_dir}' does not exist within the '{data_split}' dataset.")
            print(f"Content of the '{data_split}' dataset directory:", os.listdir(os.path.join(org_data, data_split)))
            raise FileNotFoundError(f"The subdirectory '{sub_dir}' does not exist within the '{data_split}' dataset.")

# If all checks pass, proceed with loading your dataset
print("Dataset path and subdirectories exist. Proceed with loading the dataset.")


# Custom Dataset
class DrowsyDataset(Dataset):
    def __init__(self, root='./data', split='train', transform=None, target_transform=None):
        self.root = root
        self.split = split
        self.images_folder = os.path.join(root, split, 'images')
        self.labels_folder = os.path.join(root, split, 'labels')
        self.image_files = []
        self.label_files = []
        self.transform = transform
        self.target_transform = target_transform
        self.load_data()

    def load_data(self):
        # Check if the images and labels folders exist
        if not os.path.exists(self.images_folder) or not os.path.exists(self.labels_folder):
            raise FileNotFoundError(f"Images or labels folder not found for {self.split} dataset.")

        # Get a list of all image files in the images folder
        self.image_files = [f for f in os.listdir(self.images_folder) if f.endswith('.jpg')]

        # Get a list of all label files in the labels folder
        self.label_files = [f for f in os.listdir(self.labels_folder) if f.endswith('.txt')]

    def __len__(self):
        return len(self.image_files)

    def get_image_path(self, image_file):
        return os.path.join(self.images_folder, image_file)

    def get_label_path(self, label_file):
        return os.path.join(self.labels_folder, label_file)

    def __getitem__(self, idx):
        image_file = self.image_files[idx]
        image_path = self.get_image_path(image_file)
        label_file = image_file.replace('.jpg', '.txt')
        label_path = self.get_label_path(label_file)

        # Read image
        image = cv2.imread(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Read label
        with open(label_path, 'r') as file:
            label_content = file.read()

        # Convert label to tensor
        label_tensor = torch.tensor(float(label_content), dtype=torch.float32)

        # Apply transformations
        if self.transform:
            image = self.transform(image)

        if self.target_transform:
            label_tensor = self.target_transform(label_tensor)

        return {'image': image, 'label': label_tensor}


# Image preprocessing transformation for train data
t_transformer = v2.Compose([
    v2.ToImage(),  # Convert to PIL Image format
    v2.Resize(224),  # Resize to a square of size 224x224 pixels
    v2.ToDtype(torch.uint8, scale=True),  # Convert to unsigned 8-bit integer
    v2.RandomResizedCrop(size=(512, 512), antialias=True),  # Random crop with antialiasing
    v2.RandomHorizontalFlip(),  # Horizontal random flip (data augmentation)
    v2.RandomVerticalFlip(),  # Vertical random flip (data augmentation)
    v2.RandomRotation(15),  # Rotational random flip up to 15 degrees (data augmentation)
    v2.ToDtype(torch.float32, scale=True),  # Convert to 32-bit floating-point format
    v2.ToTensor(),  # Convert to PyTorch tensor
    v2.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),  # Normalize with mean and std
])

# Image preprocessing transformation for val and test data
vt_transformer = v2.Compose([
    v2.ToImage(),
    v2.Resize(224),
    v2.ToDtype(torch.uint8, scale=True),
    v2.RandomResizedCrop(size=(512, 512), antialias=True),
    v2.ToDtype(torch.float32, scale=True),
    v2.ToTensor(),
])

# Train dataset
train_ds = DrowsyDataset(
    root=org_data,
    split='train',
    transform=t_transformer,
    target_transform=lambda x: int(x)
)

# Val dataset
val_ds = DrowsyDataset(
    root=org_data,
    split='valid',
    transform=vt_transformer,
    target_transform=lambda x: int(x)
)

# Test dataset
test_ds = DrowsyDataset(
    root=org_data,
    split='test',
    transform=vt_transformer,
    target_transform=lambda x: int(x)
)

# Train DataLoader
train_loader = DataLoader(
    train_ds,
    batch_size=128,
    shuffle=True,
    num_workers=2,
    drop_last=True
)

# Val DataLoader
val_loader = DataLoader(
    val_ds,
    batch_size=128,
    shuffle=False,
    num_workers=2,
    drop_last=False
)

# Test DataLoader
test_loader = DataLoader(
    test_ds,
    batch_size=128,
    shuffle=False,
    num_workers=2,
    drop_last=False
)