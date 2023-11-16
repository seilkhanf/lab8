import os

def list_directories_files_all(path):
    try:
        # List all directories
        print("Directories:")
        for dir_name in os.listdir(path):
            if os.path.isdir(os.path.join(path, dir_name)):
                print(dir_name)

        # List all files
        print("\nFiles:")
        for file_name in os.listdir(path):
            if os.path.isfile(os.path.join(path, file_name)):
                print(file_name)

        # List all subdirectories and files recursively
        print("\nAll Directories and Files:")
        for root, dirs, files in os.walk(path):
            for dir_name in dirs:
                print(os.path.join(root, dir_name))
            for file_name in files:
                print(os.path.join(root, file_name))

    except FileNotFoundError:
        print("no founded")