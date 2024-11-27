from PIL import Image
import numpy as np

def has_alpha_channel(image_path):
    """Check if an image has an alpha channel"""
    
    img = Image.open(image_path)
    return img.mode == 'RGBA'

def is_transparent(pixel):
    """Take an rgba pixel and return True if it's empty and False otherwise"""
    
    return np.array_equal(pixel, [0, 0, 0, 0])
    