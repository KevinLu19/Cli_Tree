import cli_tree.cli
import pathlib

from dataclasses import dataclass

@dataclass
class TreeStruct:
    TREE_PIPE: str = "│"
    TREE_TEE: str = "├──"
    TREE_ELBOW: str = "└──"

class TreeGenerator:
    def __init__(self, root_dir, dir_only = False):
        #self.CLI_CLASS = cli_tree.cli.Directories(root_dir)
        self.tree_struct = TreeStruct()
        self.root_dir = pathlib.Path(root_dir)
        self.dir_only = dir_only

    def tree_body(self, directory):
        entries = self.prepare_entries(directory)
        entries_count = len(entries)

        for index, entry in enumerate(entries):
            connector = self.tree_struct.TREE_ELBOW if (index == entries_count -1) else self.tree_struct.TREE_TEE
            
            print(entry)
            print(connector)

    def prepare_entries(self, directory):
        entries = directory.iterdir()

        if self.dir_only:
            entries = [entry for entry in entries if entry.is_dir()]
            return entries
        entries = sorted(entries, key=lambda entry: entry.is_file())
        return entries

def main():
    sample_root = "../cli_tree"
    tree = TreeGenerator(sample_root)
    tree.print_trees()

    tree_struct = TreeStruct()
    print(tree_struct.TREE_TEE)
    
if __name__ == "__main__":
    main()