import sys
import zipfile
import importlib
import os

def install_package(package):
    try:
        importlib.import_module(package)
    except ImportError:
        import sys
        !{sys.executable} -m pip install {package}

def get_file_path(filename):
      full_path = F"{BASE_PATH}{filename}"
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
        
        # Check if the file exists
        if os.path.exists(full_path):
            print(f'{filename} exists')
            
            # Check if it's a valid zip file
            if zipfile.is_zipfile(full_path):
                print(f'{filename} is a valid zip file')
                
                # automatically unzip valid zip files
                with zipfile.ZipFile(get_file_path(filename), 'r') as z:
                  # Create a progress bar
                      with tqdm(total=len(z.namelist())) as pbar:
                          for file in z.namelist():
                              z.extract(member=file, path=BASE_PATH)
                              # Update the progress bar
                              pbar.update()
            else:
                print(f'{filename} is not a valid zip file')
        else:
            print(f'{filename} does not exist')