import cli
import pathlib

class TreeGenerator:
    def __init__(self, root_dir):
        self.CLI_CLASS = cli.Directories()
        self.__TREE_PIPE = "│"
        self.__TREE_TEE = "├──"
        self.__TREE_ELBOW = "└──"
        self.__TREE_TEE_SUFFIX = "├──   "
        self.__TREE_ELBOW_SUFFIX = "└──   "
        self.root_dir = pathlib.Path(root_dir)
    
    def print_trees(self):
        cli_class_queue = self.CLI_CLASS.find_subdirectories()
        length_of_entries = len(cli_class_queue)

        for index, entry in enumerate(cli_class_queue):
            connector = self.__TREE_ELBOW if (index == length_of_entries -1) else self.__TREE_TEE
            
            print(entry)
            print(connector)


def main():
    tree = TreeGenerator()
    tree.print_trees()
    
if __name__ == "__main__":
    main()