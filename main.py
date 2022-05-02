from cli_tree import __version__
import cli_tree.cli as cli
import argparse

PARSE_MESSAGE = """

optional arguemnts: 
    -h, --help                  shows this help message and exit
    -v, --version               shows program's version number and exits
    -d, --dir-only              Generates a directory-only tree
    -o [OUTPUT_FILE], --output-file [OUTPUT_FILE]   Generate a full directory tree and save it to file.

Thanks for using my CLI Tree!
"""

def main():
    tree_cli = cli.Directories()

    # parser = argparse.ArgumentParser(description=PARSE_MESSAGE)
    # args = parser.parse_args()

    parse = argparse.ArgumentParser(description="CLI Tree. Directory tree generator.")
    parse.add_argument("ROOT_DIR", help="Genearte a full directory tree starting at ROOT_DIR")
    parse.add_argument("-v", "--version",action="version", version=__version__,help="shows program's version number and exits")
    parse.add_argument("-d", "--dir-only", action= tree_cli.find_subdirectories() ,help="Generates a directory-only tree.")
    parse.add_argument("-o [OUTPUT_FILE]", "--output-file [OUTPUT_FILE]", help="Genearte a full directory tree and save it to file.")
    args = parse.parse_args()



if __name__ == "__main__":
    main()