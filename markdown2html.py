#!/usr/bin/python3
"""
A script that takes an argument 2 strings:
First argument is the name of the Markdown file.
Second argument is the output file name..
"""
import sys
import os.path


if __name__ == "__main__":
    """Main function of the script.
    Read the Markdown file, convert it to HTML, and save it to the output file.
    """
    if len(sys.argv) < 3:
        print('Usage: ./markdown2html.py README.md README.html',
              file=sys.stderr)
        exit(1)

    if not os.path.isfile(sys.argv[1]):
        print('Missing {}'.format(sys.argv[1]), file=sys.stderr)
        exit(1)

    exit(0)
