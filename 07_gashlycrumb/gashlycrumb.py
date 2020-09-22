#!/usr/bin/env python3
"""
Author : Jeff Fillipi <jrfillipi@gmail.com>
Date   : 2020-09-22
Purpose: lookup tables
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Lookup tables',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('letter',
                        nargs='+',
                        help='Letter(s)')

    parser.add_argument('--file', '-f',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='gashlycrumb.txt',
                        help='Input file')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    letters = args.letter
    fh = args.file

    lookup_dict = {}
    for line in fh:
        lookup_dict[line[0].upper()] = line.rstrip()
    # lookup_dict = {line[0].upper(): line.rstrip() for line in fh}

    for letter in letters:
        if letter.upper() in lookup_dict:
            print(f'{lookup_dict[letter.upper()]}')
        else:
            print(f'I do not know "{letter}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
