import cli_tree.cli
import pathlib

from dataclasses import dataclass

@dataclass
class TreeStruct:
    TREE_PIPE: str = "│"
    TREE_TEE: str = "├──"
    TREE_ELBOW: str = "└──"
    # TREE_TEE_SUFFIX: string = "├──   "
    # TREE_ELBOW_SUFFIX:string = "└──   " 

class TreeGenerator:
    def __init__(self, root_dir, dir_only = False):
        #self.CLI_CLASS = cli_tree.cli.Directories(root_dir)
        self.tree_struct = TreeStruct()
        self.root_dir = pathlib.Path(root_dir)
        self.dir_only = dir_only
    
    # def print_trees(self):
    #     cli_class_queue = self.CLI_CLASS.find_subdirectories()
    #     length_of_entries = len(cli_class_queue)

    #     for index, entry in enumerate(cli_class_queue):
    #         connector = self.tree_struct.TREE_ELBOW if (index == length_of_entries -1) else self.tree_struct.TREE_TEE
            
    #         print(entry)
    #         print(connector)

    def tree_body(self, directory):
        entries = self.prepare_entries(directory)
        entries_count = len(entries)

        for index, entry in enumerate(entries):
            connector = self.tree_struct.TREE_ELBOW if (index == entries_count -1) else self.tree_struct.TREE_TEE
            
            print(entry)
            print(connector)

def main():
    sample_root = "../cli_tree"
    tree = TreeGenerator(sample_root)
    tree.print_trees()

    tree_struct = TreeStruct()
    print(tree_struct.TREE_TEE)
    
if __name__ == "__main__":
    main()