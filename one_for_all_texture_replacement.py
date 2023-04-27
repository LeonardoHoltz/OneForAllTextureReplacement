import configparser
import os
import shutil
import time

# Read the configuration file
config = configparser.ConfigParser()
config.read('config.ini')

dumps_folder = config.get('TextureReplConfig', 'dumps_folder')
replacements_folder = config.get('TextureReplConfig', 'replacements_folder')
duplicate_file = config.get('TextureReplConfig', 'duplicate_file')

while True:
    # Get the list of PNG files in the folder
    png_files = [f for f in os.listdir(dumps_folder) if f.endswith('.png')]

    # Check for new files
    for file in png_files:
        # Check if the file has already been processed
        if not os.path.exists(os.path.join(dumps_folder, file + ".processed")):
            # Copy the name of the file
            filename = os.path.splitext(file)[0]

            # Duplicate the pre-determined file with the new name and save it in the same folder
            new_file = os.path.join(replacements_folder, filename + ".png")
            shutil.copy(duplicate_file, new_file)

            # Mark the original file as processed
            open(os.path.join(dumps_folder, file + ".processed"), "w").close()

    # Wait for a bit before checking again
    time.sleep(1)