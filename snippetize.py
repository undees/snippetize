#!/usr/bin/env python

from snippetize.snippetizer import Snippetizer
import sys

if __name__ == '__main__':
    if (len(sys.argv) != 4):
        sys.stderr.write('Usage: snippetize IN.key \
OUT.key CONFIG.py\n')
        exit(-1)

    key_file, out_file, config_file = sys.argv[1:]

    snippetizer = Snippetizer(key_file, out_file, config_file)
    snippetizer.snippetize()
