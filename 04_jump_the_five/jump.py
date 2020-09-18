#!/usr/bin/env python3
"""
Author : Jeff Fillipi <jrfillipi@gmail.com>
Date   : 2020-09-18
Purpose: Jump the Five
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Jump the Five',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='A string input string with numbers to be encoded')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text

    encoder = {'0': '5', '1': '9', '2': '8', '3': '7', '4': '6', '5': '0',
               '6': '4', '7': '3', '8': '2', '9': '1'}

    print(''.join([encoder.get(char, char) for char in text]))

    # for char in text:
    #     print(encoder.get(char, char), end="")


# --------------------------------------------------
if __name__ == '__main__':
    main()
