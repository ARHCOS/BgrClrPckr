import os

def get_png_files(directory):
    """Takes the name of a directory and returns the name of all png files inside"""
    
    png_files = []
    for filename in os.listdir(directory):
        if filename.endswith('.png'):
            png_files.append(filename)
    return png_files

def create_directory(directory):
    """Create a folder in the the directory"""
    
    if not os.path.exists(directory):
        os.makedirs(directory)
        print("\nThe folder has been created.\n")
    else:
        print("\nThe folder already exist.\n")
