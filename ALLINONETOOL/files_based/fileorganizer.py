# file_organizer.py
import os
import shutil

def organize_files(source_folder, destination_folder):
    # Walk through all files and subdirectories in the source folder
    for root, _, files in os.walk(source_folder):
        for file in files:
            # Create the full path of the file
            file_path = os.path.join(root, file)

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

if __name__ == "__main__":
    # Specify source and destination folders
    source_folder = "your/source/folder"
    destination_folder = "your/destination/folder"

    # Call the organize_files function
    organize_files(source_folder, destination_folder)
