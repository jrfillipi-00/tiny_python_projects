#!/usr/bin/env python3
"""
Author : Jeff Fillipi <jrfillipi@gmail.com>
Date   : 2020-09-18
Purpose: Picnic Game
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic Game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('item',
                        metavar='str',
                        help='Item(s) to bring',
                        nargs='+')

    parser.add_argument('-s',
                        '--sorted',
                        help='Sorts the listed items.',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items = args.item
    num = len(items)

    if args.sorted:
        items.sort()

    bringing = ''
    if num > 2:
        bringing = f'{", ".join(items[:-1])}, and {items[-1]}'
    elif num == 2:
        bringing = ' and '.join(items)
    else:
        bringing = items[0]

    print(f'You are bringing {bringing}.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
