import os
from pathlib import Path
from glob import glob

import tree_gen

class Directories:
    def __init__(self, root_directory):
        self.root_dir = tree_gen.TreeGenerator(root_directory)

    def find_root_dir(self):
        current_file_path = os.path.dirname(__file__)
        parent_of_current_file = os.path.dirname(current_file_path)

        PROJECT_ROOT = os.path.basename(parent_of_current_file)
        return PROJECT_ROOT

    def find_subdirectories(self):
        subdirectories_queues = []
        path = Path(".")
        for subdirectories in path.iterdir():
            if subdirectories.is_dir():
                convert_window_path_to_string = subdirectories.__str__()
                subdirectories_queues.append(convert_window_path_to_string)
                #print(subdirectories)

        # print(subdirectories_queues)

        return subdirectories_queues

    def list_files_in_subdirectories(self, path):
        subdirectory_item = list(path.glob("**/*.py"))

        print(subdirectory_item)

def main():
    path = os.getcwd()
    current_directory = os.path.exists(path)

    direct = Directories()
    # print(direct.list_files_in_subdirectories(path))
    direct.find_subdirectories()

if __name__ == "__main__":
    main()