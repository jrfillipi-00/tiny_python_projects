#!/usr/bin/env python3
"""
Author : Jeff Fillipi <jrfillipi@gmail.com>
Date   : 2020-09-21
Purpose: Howler: Working with files and STOUT
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler: Working with files and STOUT',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        help='Input string or file name')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='')

    args = parser.parse_args()

    # Checks if the text input is a file.  If true,
    # changes args.text to the string contents of the given file.
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()
    # Book mentions that this is not best-practice for large files.  What is?

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text
    out_file_name = args.outfile

    if os.path.isfile(text):
        fh_in = open(text)
        out_text = fh_in.read().rstrip().upper()
        fh_in.close()
    else:
        out_text = text.upper()

    # if out_file is not '', then open outfile, print to it and close
    if out_file_name:
        fh_out = open(out_file_name, 'wt')
        print(out_text, file=fh_out)
        fh_out.close()
        out_text = ''

    print(f'{out_text}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
