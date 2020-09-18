#!/usr/bin/env python3
"""tests for jump.py"""

import os
from subprocess import getstatusoutput

prg = './jump.py'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_numbers():
    """test numbers"""

    rv, out = getstatusoutput(f'{prg} 1234567890')
    assert rv == 0
    assert out == '9876043215'


# --------------------------------------------------
def test_sentence():
    """test an input sentence"""

    rv, out = getstatusoutput(f'{prg} "That number to call is 098-765-4321."')
    assert rv == 0
    assert out.rstrip() == 'That number to call is 512-340-6789.'


# --------------------------------------------------
def test_round_trip():
    """test round-trip"""

    rv1, out = getstatusoutput(f'{prg} 123-456-7890')
    rv2, out = getstatusoutput(f'{prg} {out}')
    assert rv1 == 0
    assert rv2 == 0
    assert out == '123-456-7890'
