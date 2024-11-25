from PIL import Image
import numpy as np

# Loading the Image

image_name = input('Enter the image name (without .png) : ')+'.png'
image = Image.open(image_name)

# Puting the Image into a matrix

matrix = np.array(image, dtype=np.float32)

# Useful infos

height, width, _ = matrix.shape

print(f'Loaded {image_name} : {height}x{width}')

# Setting up colors

red = [255,0,0]
green = [0,255,0]
blue = [0,0,255]

selected_bgr_color = input('Enter your prefered color for the background (r, g or b) : ')

if selected_bgr_color in ['r', 'red', 'R']:
    r1, g1, b1 = red
    
elif selected_bgr_color in ['g', 'green', 'G']:
    r1, g1, b1 = green
    
elif selected_bgr_color in ['b', 'blue', 'B']:
    r1, g1, b1 = blue

else:
    raise ValueError('Wrong color for the background')

total_pixels = height*width

# Doing the big brain math

def has_alpha_channel(image_name):
    """Check if an image has an alpha channel"""
    img = Image.open(image_name)
    
    if img.mode == 'RGBA' or img.mode == 'LA':
        return True
    return False

def rgb_distance(r1,g1,b1,r2,g2,b2):
    """Calculate the Euclidian distance between a pixel from the image and the one from the background"""
    
    return np.sqrt(((r1-r2)**2)+((g1-g2)**2)+((b1-b2)**2))

def too_close(image):
    """Apply the equation to every pixel of an image that doesn't have an alpha channel. Return True if any pixel is too close and False if not"""
    
    n_pixel = 0
            
    for i in range(height):
        for j in range(width):
            r2,g2,b2= image[i][j]
            n_pixel += 1
            print(f'\rPixel number {n_pixel} out of {total_pixels}', end='', flush=True)
            if rgb_distance(r1,g1,b1,r2,g2,b2) <= 100:
                return True
    return False
    
def too_close_alpha(image):
    """Apply the equation to every pixel of an image that have an alpha channel. Return True if any pixel is too close and False if not"""
    
    n_pixel = 0
            
    for i in range(height):
        for j in range(width):
            r2,g2,b2,_= image[i][j]
            n_pixel += 1
            print(f'\rPixel number {n_pixel} out of {total_pixels}', end='', flush=True)
            if rgb_distance(r1,g1,b1,r2,g2,b2) <= 100:
                return True
    return False

# Final result for the user
            
print('Calculating...')

if has_alpha_channel(image_name) == False:
    if too_close(matrix) == False:
        print('\nThe background color you selected doesn\'t interfere with your image')
    
    else:
        print('\nThe background color you selected may interfere with the image, try with a different one')

else:
    if too_close_alpha(matrix) == False:
        print('\nThe background color you selected doesn\'t interfere with your image')
    
    else:
        print('\nThe background color you selected may interfere with the image, try with a different one')
    
print('Press any key to exit...')
input()
