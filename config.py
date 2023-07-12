import sys
import zipfile
import os
import importlib
import subprocess

def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def get_file_path(base_path,filename):
      full_path = F"{base_path}{filename}"
      return full_path

try:
    from tqdm import tqdm
except ImportError:
    # If tqdm is not installed, install it
    install_package('tqdm')
    from tqdm import tqdm

def config_data(base_path, zipfiles):

    for filename in zipfiles:
        full_path = os.path.join(base_path, filename)

        # Derive the name of the expected output directory
        expected_dir = os.path.join(base_path, filename.split('.')[0]) 

        # If the expected directory already exists, skip extraction
        if os.path.isdir(expected_dir):
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
                          for file in z.namelist():
                              z.extract(member=file, path=base_path)
                              # Update the progress bar
                              pbar.update()
            else:
                print(f'{filename} is not a valid zip file')
        else:
            print(f'{filename} does not exist')
    print('Finished!')