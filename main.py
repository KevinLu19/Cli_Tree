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

    parse = argparse.ArgumentParser(description="CLI Tree for directory.")
    parse.add_argument("-v", action="version", version=__version__,help="shows program's version number and exits")
    args = parse.parse_args()

    print (args)


if __name__ == "__main__":
    main()