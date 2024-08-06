import os

def rename_files_in_folders(root_folder):
    # Walk through all files and subdirectories in the root folder
    for root, dirs, files in os.walk(root_folder):
        for file in files:
            # Create the full path of the file
            file_path = os.path.join(root, file)

            # Get the parent folder's name
            folder_name = os.path.basename(root)

            # Construct the new file name with the folder's name
            new_file_name = f"{folder_name}_{file}"

            # Construct the new file path
            new_file_path = os.path.join(root, new_file_name)

            # Rename the file
            os.rename(file_path, new_file_path)

if __name__ == "__main__":
    # Specify the root folder containing subfolders with files
    root_folder = "your/root/folder"

    # Call the rename_files_in_folders function
    rename_files_in_folders(root_folder)
