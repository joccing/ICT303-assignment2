# ICT303 Assignment2
Hi Students of ICT303!

This code allows you to uncompress the training and test data for **Assignment 2** into a folder on your Google Drive.

Start by
1. Going to the [kaggle site](https://www.kaggle.com/c/dog-breed-identification/data) and download the zip file.
2. Upload the *dog-breed-identification.zip* file to a folder in Google drive, say **/content/gdrive/My Drive/path/to/your/assignment/**
3. Create a cell at the beginning of your **Colab/Jupyter/VSCode/** notebook, and copy and paste this code there:

```python
def is_running_in_colab():
    try:
        from google.colab import _ipython as ip
        return True
    except ImportError:
        return False

try:
  if is_running_in_colab():
    print("Running in Google Colab")
    from google.colab import drive
    drive.mount('/content/gdrive',force_remount=True)
  else:
    print("Running in Jupyter or VSCode")

  import requests
  url = 'https://raw.githubusercontent.com/joccing/ICT303-assignment2/master/config.py'
  r = requests.get(url, allow_redirects=True)
  open('config.py', 'wb').write(r.content)

except ModuleNotFoundError:
  pass

# PLEASE MODIFY BASE PATH
BASE_PATH = F"/content/gdrive/My Drive/path/to/your/assignment/"

# Name of zip files
zipfiles = ['dog-breed-identification.zip']

from config import *
DOWNLOADED = config_data(BASE_PATH,zipfiles, ['train','test','labels.csv'])
assert DOWNLOADED == 20581 or DOWNLOADED < 0
assert check_all(BASE_PATH, ['train','test','labels.csv']) == True
```

4. Modify the Base Path in the code above and execute the cell using *Shift-Return*.  It should start expanding the zip file. 