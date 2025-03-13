import os
import shutil

def copy_static(source_dir, dest_dir):
    # Delete destination directory if it exists
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)

    # Create destination directory
    os.mkdir(dest_dir)

    # Get all files and directories in source
    items = os.listdir(source_dir)

    # Iterate through all items
    for item in items:
        # Create full paths
        source_item = os.path.join(source_dir, item)
        dest_item = os.path.join(dest_dir, item)

        # Check if it's a file or directory
        if os.path.isfile(source_item):
            # It's a file - copy it
            print(f"Copying file: {source_item} to {dest_item}")
            shutil.copy(source_item, dest_item)
        else:
            # It's a directory - recursively copy it
            print(f"Copying directory: {source_item} to {dest_item}")
            copy_static(source_item, dest_item)

def main():
    copy_static("static", "public")


main()
