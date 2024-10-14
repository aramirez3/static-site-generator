from textnode import TextNode

from os import path, listdir, mkdir

from shutil import copy, rmtree

# delete all contents from /public dir
# get all folders from /static
# create folder structure in /public dir
# get items for each folder in static
# copy contents to static

def reset_public_folder():
    public_folder_path = "public"
    rmtree(public_folder_path)
    print(f"Deleted '{public_folder_path}'")
    mkdir(public_folder_path)
    print(f"Created folder '{public_folder_path}'")
    
def copy_folder_contents(target_folder = "static", destination_folder = "public"):
    folder_content = listdir(target_folder)
    for item in folder_content:
        current_item_path = f"{target_folder}/{item}"
        if path.isdir(current_item_path):
            new_folder = f"{destination_folder}/{item}"
            mkdir(new_folder)
            print(f"Created folder {new_folder}")
            copy_folder_contents(current_item_path, new_folder)
        else:
            print(f"Copying {target_folder}/{item} to {destination_folder}/{item}")
            copy(f"{target_folder}/{item}", f"{destination_folder}/{item}")
    
def main():
    reset_public_folder()
    copy_folder_contents()

main()