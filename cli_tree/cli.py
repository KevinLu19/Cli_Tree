import os
from pathlib import Path

TREE_PIPE = "│"
TREE_TEE = "├──"
TREE_ELBOW = "└──"

class Directories:
    def __init__(self):
        self.subdirectory_queues = []

    def find_root_dir(self):
        current_file_path = os.path.dirname(__file__)
        parent_of_current_file = os.path.dirname(current_file_path)

        PROJECT_ROOT = os.path.basename(parent_of_current_file)
        return PROJECT_ROOT

    def find_subdirectories(self):
        
        path = Path(".")
        for subdirectories in path.iterdir():
            if subdirectories.is_dir():
                self.subdirectory_queues.append(subdirectories)
                print(subdirectories)
        
        return self.subdirectory_queues
    
    def return_subdirectories_queue(self):
        return self.subdirectory_queues if (len(self.subdirectory_queues)> 0) else False

    def list_files_in_subdirectories(self, path):
        subdirectory_item = list(path.glob("**/*.py"))

        print(subdirectory_item)

def main():
    path = os.getcwd()
    current_directory = os.path.exists(path)

    direct = Directories()
    print(direct.list_files_in_subdirectories(path))

if __name__ == "__main__":
    main()