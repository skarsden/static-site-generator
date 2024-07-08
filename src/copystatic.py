import os
import shutil

def copy_static(source, dest):
    #If the source isn't valid/not given
    if not os.path.exists(source):
        raise ValueError("Source file does not exist")
    #If a valid destination isn't found, make one
    if not os.path.exists(dest):
        os.mkdir(f"./{dest}")
    #iterate through each file/directory in source
    for item in os.listdir(source):
        #if the item is a file: copy it, if it's a directory: recurse
        if os.path.isfile(f"{source}/{item}"):
            shutil.copy(f"{source}/{item}", dest)
        else:
            os.mkdir(f"{dest}/{item}")
            copy_static(f"{source}/{item}", f"{dest}/{item}")
    print(f"copied contents from {source} to {dest}")