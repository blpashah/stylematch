from PIL import Image
import numpy as np

def convert_raw_to_rgb(uploaded_file):
    image = Image.open(uploaded_file).convert("RGB")
    return np.array(image)
