import os
import shutil

# Define the __pycache__ directory name and the default base directory
PYCACHE_DIR_NAME = '__pycache__'
DEFAULT_BASE_DIRECTORY = r'C:\Users\liam\Documents\code\python\Code'

def removefolders(base_directory):
    """
    Recursively delete all directories named PYCACHE_DIR_NAME under the given base directory.
    
    Args:
        base_directory (str): The root directory to start searching for PYCACHE_DIR_NAME folders.
    """
    for root, dirs, files in os.walk(base_directory, topdown=False):
        for dir_name in dirs:
            if dir_name == PYCACHE_DIR_NAME:
                dir_path = os.path.join(root, dir_name)
                try:
                    shutil.rmtree(dir_path)
                    print(f"Deleted {PYCACHE_DIR_NAME} directory at {dir_path}")
                except Exception as e:
                    print(f"Error deleting {dir_path}: {e}")

def main():
    # Prompt user to choose between the default directory or a custom one
    choice = input("Choose the directory option:\n1. Use default directory\n2. Enter custom directory path\nEnter your choice (1 or 2): ")
    
    if choice == '1':
        base_directory = DEFAULT_BASE_DIRECTORY
    elif choice == '2':
        base_directory = input("Enter the custom directory path: ")
    else:
        print("Invalid choice. Exiting.")
        return
    
    if not os.path.isdir(base_directory):
        print("The provided directory path is not valid.")
        return

    removefolders(base_directory)

if __name__ == "__main__":
    main()
