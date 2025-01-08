import os
from torchvision import datasets, transforms
from PIL import Image  # Import PIL for saving images

# 下载MNIST
# Define the transform
transform = transforms.Compose(
    [transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))]
)

# Load the MNIST dataset
test_dataset = datasets.MNIST(
    root='./data', train=False, download=True, transform=transform
)

# Directories for saving data
data_dir = 'data/MNIST'
image_dir = os.path.join(data_dir, 'features')
os.makedirs(data_dir, exist_ok=True)
os.makedirs(image_dir, exist_ok=True)

# Open the labels file for writing
with open(os.path.join(data_dir, 'test_labels.txt'), 'w') as label_file:
    for i in range(len(test_dataset)):
        img, label = test_dataset[i]
        
        # Convert the tensor to a PIL image
        img_pil = transforms.ToPILImage()(img)
        
        # Save the image as PNG
        img_pil.save(os.path.join(image_dir, f'test_{i}.png'))
        
        # Write the label to the text file
        label_file.write(f'test_{i}.png {label}\n')

#下载cifar10
transform = transforms.Compose(
  [transforms.ToTensor(), transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))]
)

test_dataset = datasets.CIFAR10(
  root='./data', train=False, download=True, transform=transform
)

data_dir = 'data/CIFAR10'
image_dir = os.path.join(data_dir, 'features')
os.makedirs(data_dir, exist_ok=True)
os.makedirs(image_dir, exist_ok=True)

# Open the labels file for writing
with open(os.path.join(data_dir, 'test_labels.txt'), 'w') as label_file:
    for i in range(len(test_dataset)):
        img, label = test_dataset[i]
        
        # # Convert the tensor to a PIL image
        # img_pil = transforms.ToPILImage()(img)
        
        # # Save the image as PNG
        # img_pil.save(os.path.join(image_dir, f'test_{i}.png'))
        
        # # Write the label to the text file
        # label_file.write(f'test_{i}.png {label}\n')
        img.save(os.path.join(image_dir, f'test_{i}.png'))
        label_file.write(f'test_{i}.png {label}\n')