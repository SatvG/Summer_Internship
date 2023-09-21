import os
import shutil

# Set the username and path to the BenignReport folder
username = 'abc'
path = f'/home/{username}/Documents/BenignReport'

# Iterate over the subfolders
for i in range(1, 501):
  subfolder_path = os.path.join(path, str(i))
  # Check if the subfolder exists
  if os.path.exists(subfolder_path):
    print(f'Processing subfolder {i}...')
    # Iterate over the files and folders in the subfolder
    for item in os.listdir(subfolder_path):
      item_path = os.path.join(subfolder_path, item)
      # Check if the item is not named "reports"
      if item != 'reports':
        # Delete the item
        if os.path.isfile(item_path):
          print(f'Deleting file {item}...')
          os.remove(item_path)
        elif os.path.isdir(item_path):
          print(f'Deleting folder {item}...')
          shutil.rmtree(item_path)
print('Done!')
