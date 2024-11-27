from scripts.crop import has_alpha_channel, is_transparent
from scripts.utility import get_png_files, create_directory
from PIL import Image
#import time
import numpy as np


# Setting up colors

red = [255,0,0]
green = [0,255,0]
blue = [0,0,255]

selected_bgr_color = input('Enter your prefered color for the background (r, g or b) : ')
print(f'\nPreceeding with {selected_bgr_color}')


if selected_bgr_color in ['r', 'red', 'R']:
    r1, g1, b1 = red
    
elif selected_bgr_color in ['g', 'green', 'G']:
    r1, g1, b1 = green
    
elif selected_bgr_color in ['b', 'blue', 'B']:
    r1, g1, b1 = blue

else:
    raise ValueError('Wrong color for the background')



# Useful things

create_directory(r'./PUT IMAGES HERE')

png_files = get_png_files(r'./PUT IMAGES HERE')



# Doing the big brain math

def rgb_distance(r1,g1,b1,r2,g2,b2):
    """Calculate the Euclidian distance between a pixel from the image and the one from the background"""
    
    return np.sqrt(((r1-r2)**2)+((g1-g2)**2)+((b1-b2)**2))

def too_close(image):
    """Apply the equation to every pixel of an image that doesn't have an alpha channel. Return True if any pixel is too close and False if not"""

    height, width, _ = matrix.shape

    print(f'Loaded {image_name} : {height}x{width}\n')
    
    n_pixel = 0
    total_pixels = height*width
            
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
    total_pixels = 0

    height, width, _ = matrix.shape

    print(f'Loaded {image_name} : {height}x{width}\n')
    
    for p1 in range(height):
        for p2 in range(width):
            if is_transparent(image[p1][p2]) == False:
                total_pixels += 1
            
    for i in range(height):
        for j in range(width):
            if is_transparent(image[i][j]) == False:
                
                r2,g2,b2,_= image[i][j]
                n_pixel += 1
                print(f'\rPixel number {n_pixel} out of {total_pixels}', end='', flush=True)
                
                if rgb_distance(r1,g1,b1,r2,g2,b2) <= 100:
                    return True
    return False
 


# Now the big brain math times the number of images in the folder

problematic_images = []

print('Calculating...\n')

for i in png_files:
    
    condition = False
    
    image_name = i
    
    image_path = r'./PUT IMAGES HERE/' + image_name

    image = Image.open(image_path)

    matrix = np.array(image, dtype=np.float32)
    
    if has_alpha_channel(image_path) == True:
        print(f'Alpha Channel detected for {i} : Proceeding with optimization\n')
        if too_close_alpha(matrix) == False:
            print('\nThe background color you selected doesn\'t interfere with your image\n')
        
        else:
            print('\nThe background color you selected may interfere with the image, try with a different one\n')
            
    
    elif has_alpha_channel(image_path) == False:
        if too_close(matrix) == False:
            print('\nThe background color you selected doesn\'t interfere with your image\n')
        
        else:
            print('\nThe background color you selected may interfere with the image, try with a different one\n')
            problematic_images.append[i]
            
if len(problematic_images) != 0:
    print('\nHere are the problematic images : ', problematic_images)

else:
    print('All of your images are compatible with your background\n') 
            
print('Press any key to exit...')
input()