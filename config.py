import sys
import zipfile
import os
import importlib
import subprocess

try:
    from tqdm import tqdm
except ImportError:
    # If tqdm is not installed, install it
    install_package('tqdm')
    from tqdm import tqdm

def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def get_file_path(base_path,filename):
    full_path = F"{base_path}{filename}"
    return full_path

def check_all(path, expected_names):
    # Get the actual names of all files and directories in the path
    actual_names = os.listdir(path)
    # Map the actual names to see if they are in the expected names, and convert the result to a list
    mapped = list(map(lambda x: x in actual_names, expected_names))    
    # Check if all the expected names were found
    return len(mapped) == len(expected_names) and all(mapped)

def config_data(base_path, zipfiles, expected_names=[]):

    print(f'Folder: {base_path}')
    total = 0

    if expected_names and check_all(base_path, expected_names):
        print(f'Files expected already exist. Skipping extraction...')
        total = -1 # signify that all seems fine even though none are extracted
    else:
        for filename in zipfiles:
            full_path = os.path.join(base_path, filename)

            # Derive the name of the expected output directory
            expected_output = os.path.join(base_path, filename.split('.')[0])
            if filename.endswith(".zip") and not filename.endswith(".csv.zip"):
                expected_output += "/"

            # If the expected directory already exists, skip extraction
            if os.path.isdir(expected_output):
                print(f'Output directory for {filename} already exists. Skipping extraction...')
                continue

            # Check if the file exists
            if os.path.exists(full_path):
                print(f'{filename} exists')
                
                # Check if it's a valid zip file
                if zipfile.is_zipfile(full_path):
                    print(f'{filename} is a valid zip file')
                    
                    # automatically unzip valid zip files
                    with zipfile.ZipFile(get_file_path(base_path,filename), 'r') as z:
                    # Create a progress bar
                        with tqdm(total=len(z.namelist())) as pbar:
                                # print('\n')
                                for file in z.namelist():
                                    # Skip any "__MACOSX" files or directories
                                    if "__MACOSX" not in file:
                                        # print(f'Extracting: {file}')
                                        z.extract(member=file, path=base_path)
                                        # Update the progress bar
                                        pbar.update()
                                        total += 1
                else:
                    print(f'{filename} is not a valid zip file')
                    return total
            else:
                print(f'{filename} does not exist')
                return total

    print('\nFinished!')
    return total