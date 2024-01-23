import os
import shutil
import cookiecutter

def move_files_to_parent_folder(folder_path: str) -> None:
    """
    Move all files in selected folder to the parent folder. 

    Args:
        folder_path (str): path to the folder all file need to be moved from.
    """

    # Check if the provided path is a directory
    if not os.path.isdir(folder_path):
        print(f"{folder_path} is not a valid directory.")
        return

    # Get a list of all files in the folder
    files = [f for f in os.listdir(folder_path)]

    # Move each file to the parent folder
    for file_name in files:
        source_path = os.path.join(folder_path, file_name)
        destination_path = os.path.join(os.path.dirname(folder_path), file_name)
        shutil.move(source_path, destination_path)
    
    # Remove folder
    # os.remove(folder_path)

# Get right folder from cookiecutter
folder_to_move = '../' + '{{cookiecutter.project_slug}}'

if( {{cookiecutter.is_existing_project}}):
    move_files_to_parent_folder(folder_to_move)