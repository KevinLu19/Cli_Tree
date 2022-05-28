from cli_tree import __version__
import cli_tree.cli as cli
import argparse
import pathlib
import sys

def argument_handler():
    parser = argparse.ArgumentParser(
        prog="cli tree", 
        description="Directory tree generator.", 
        epilog="Thanks for using my CLI Tree.")

    parser.add_argument(
        "root",
        metavar="ROOT_DIR",
        nargs="?",
        default=".",
        help="Generate a full directory tree starting at ROOT_DIR"
    )

    parser.version = f"CLI Tree {__version__}"
    parser.add_argument("-v", "--version", action="version", help="shows program's version number and exits")

    parser.add_argument("-d", "--dir-only", help="Generates a directory-only tree.")
    parser.add_argument("-o[OUTPUT_FILE]", metavar= "--output-file [OUTPUT_FILE]", help="Genearte a full directory tree and save it to file.")

    return parser.parse_args()

def main():
    command_line_argument = argument_handler()
    root_dir = pathlib.Path(command_line_argument.root)

    if not root_dir.is_dir():
        print("This is not a directory/ directory does not exist.")
        sys.exit()

    tree = cli.Directories(root_dir)
    print(tree.find_subdirectories())

if __name__ == "__main__":
    main()