import cli

class TreeGenerator:
    __TREE_PIPE = "│"
    __TREE_TEE = "├──"
    __TREE_ELBOW = "└──"

    def __init__(self, ):
        self.CLI_CLASS = cli.Directories()
    
    def print_trees(self):
        cli_class_queue = self.CLI_CLASS.return_subdirectories_queue()

        print (cli_class_queue)


def main():
    tree = TreeGenerator()
    tree.print_trees()
    
if __name__ == "__main__":
    main()