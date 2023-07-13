# ICT303 Assignment2
Hi Students of ICT303!

This code allows you to uncompress the training and test data for **Assignment 2** into a folder on your Google Drive.

Start by
1. Going to the [kaggle site](https://www.kaggle.com/c/dog-breed-identification/data) and download the zip file.
2. Upload the *dog-breed-identification.zip* file to a folder in Google drive, say **/content/gdrive/My Drive/path/to/your/assignment/**
3. Create a cell at the beginning of your **Colab/Jupyter/VSCode/** notebook, and copy and paste this code there:

```python
import importlib

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

  headers = {
    'Cache-Control': 'no-cache',
    'Pragma': 'no-cache',
    }
    
  r = requests.get(url, allow_redirects=True, headers=headers)
  open('config.py', 'wb').write(r.content)

except ModuleNotFoundError:
  pass

# PLEASE MODIFY BASE PATH, call the folder 'kaggle_dog' as below
BASE_PATH = F"/content/gdrive/My Drive/path/to/your/assignment/kaggle_dog/"
# Name of zip files that you put into the path above
zipfiles = ['dog-breed-identification.zip']

from config import *
importlib.reload(sys.modules['config'])
from config import *

DOWNLOADED = config_data(BASE_PATH,zipfiles, ['train','test','labels.csv'])
assert DOWNLOADED == 20581 or DOWNLOADED < 0
assert check_all(BASE_PATH, ['train','test','labels.csv']) == True
```

4. Modify the Base Path in the code above and execute the cell using *Shift-Return*.  It should start expanding the zip file. 

**IMPORTANT**
The above steps will uncompress the data into your Google Colab mounted version of your Google Drive folder.  I say 'version' because
they are two separate systems and what you see on Google Colab may not be what you see on Google Drive.  For large amount of files, this
will take some time to sync.  **If** you happen to close your Google Colab notebook before this syncing is complete, *all* the files
in progress of being synced will end up in your Google Drive bin.

If you want to force the sync, you can run the code below in another cell, but this takes **very very** long (given we have 20k+ files, all 
traveling through the internet).  On my laptop, it took **around 1.5 hours**.  There seems to be no way to track its progress as of this time as 
Google Colab and Google Drive are two separate independent systems.

```python
if is_running_in_colab():
    print('Syncing Google Colab and Google Drive..')
    from google.colab import drive
    drive.flush_and_unmount()
    print('Done.')
```