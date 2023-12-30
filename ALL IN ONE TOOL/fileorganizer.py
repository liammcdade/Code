# file_organizer.py
import os
import shutil

def organize_files(source_folder, destination_folder):
    # Get a list of all files in the source folder
    files = os.listdir(source_folder)

    for file in files:
        # Create the full path of the file
        file_path = os.path.join(source_folder, file)

        if os.path.isfile(file_path):
            # Get the file extension
            _, file_extension = os.path.splitext(file)

            # Define destination folder based on file extension
            destination_folder_path = os.path.join(destination_folder, file_extension[1:])

            # Create the destination folder if it doesn't exist
            if not os.path.exists(destination_folder_path):
                os.makedirs(destination_folder_path)

            # Construct the new file path
            new_file_path = os.path.join(destination_folder_path, file)

            # Move the file to the destination folder
            shutil.move(file_path, new_file_path)
