import os
from pathlib import Path

TREE_PIPE = "│"
TREE_TEE = "├──"
TREE_ELBOW = "└──"

class Directories:
    def __init__(self):
        pass

    def find_root_dir(self):
        PROJECT_ROOT = os.path.dirname(__file__)
        return PROJECT_ROOT

    def find_subdirectories(self):
        path = Path(".")
        for subdirectories in path.iterdir():
            if subdirectories.is_dir():
                print(subdirectories)
                #print(self.find_root_dir())
                # print ("|")
    
    def list_files_in_subdirectories(self, path):
        subdirectory_item = list(path.glob("**/*.py"))

        print(subdirectory_item)

def main():
    path = os.getcwd()
    current_directory = os.path.exists(path)

    print ("The base name is: ", current_directory)

    if path == "hello":
        print ("inside an non existant directory")

if __name__ == "__main__":
    main()