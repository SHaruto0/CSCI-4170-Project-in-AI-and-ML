# pip install kagglehub

import kagglehub
import os

# Get current working directory
current_dir = os.getcwd()

# Download latest version and save it in the current directory
path = kagglehub.dataset_download("muratkokludataset/rice-image-dataset")

print("Path to dataset files:", path)
