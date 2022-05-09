from cli_tree import __version__
import cli_tree.cli as cli
import argparse

def cli_arg():
    tree_cli = cli.Directories()
    parser = argparse.ArgumentParser(prog="cli tree", description="Directory tree generator.", epilog="Thanks for using my CLI Tree.")

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

    parser.parse_args()

def main():
 
    cli_arg()


if __name__ == "__main__":
    main()