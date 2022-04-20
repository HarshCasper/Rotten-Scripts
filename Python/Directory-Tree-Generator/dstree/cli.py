import pathlib
import argparse
import sys

from . import __version__
from .dstree import DirTree

def main():
    args = parse_args()
    root_dir = pathlib.Path(args.root_dir)
    if not root_dir.is_dir():
        print("Entered directory is invalid!! ")
        sys.exit()
    tree = DirTree(root_dir)
    tree.generate()


def parse_args():
    parser = argparse.ArgumentParser(
        prog = "tree",
        description = "DS Tree, a directory tree generator.",
        epilog = "Thank you for using dstree!!"
    )

    parser.version = f"ds tree v{__version__}"
    parser.add_argument("-v","--version", action = "version")
    parser.add_argument(
        "root_dir",
        metavar = "ROOT_DIR",
        nargs = "?",
        default = ".",
        help = "Generate directory tree starting at ROOT_DIR"
    )
    return parser.parse_args()
    