from textnode import TextNode
from template import generate_pages_recursive

from os import path, listdir, mkdir

from shutil import copy, rmtree

def reset_public_folder():
    public_folder_path = "public"
    if path.exists(public_folder_path):
        rmtree(public_folder_path)
    print(f"Deleted '{public_folder_path}'")
    mkdir(public_folder_path)
    print(f"Created folder '{public_folder_path}'")
    
def copy_folder_contents(target_folder = "static", destination_folder = "public"):
    folder_content = listdir(target_folder)
    for item in folder_content:
        current_item_path = path.join("", target_folder, item)
        if path.isdir(current_item_path):
            dest_folder = path.join("", destination_folder, item)
            if not path.exists(dest_folder):
                mkdir(dest_folder)
                print(f"Created folder {dest_folder}")
            copy_folder_contents(current_item_path, dest_folder)
        else:
            copy(f"{target_folder}/{item}", f"{destination_folder}/{item}")
            print(f"Copied {target_folder}/{item} to {destination_folder}/{item}")

def generate_site():
    generate_pages_recursive('content', 'template.html', 'public')
    
def main():
    reset_public_folder()
    generate_site()
    copy_folder_contents()

main()