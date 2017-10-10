#!/usr/bin/env python3

import argparse
import os
import sys

"""
input is a list of file_path
outout is a list of lane_barcode, dir_path, file_name and file_path
using standard I/O files
"""

# TODO
# show help doc
parser = argparse.ArgumentParser(description=__doc__,
                 formatter_class=argparse.RawDescriptionHelpFormatter)

# parser = argparse.ArgumentParser(description=__doc__)
parser.parse_args()  # just to show help if the user wants it

for line in sys.stdin:
# for line in f:
    line = line.rstrip()
    sample_dir = os.path.dirname(line)
    # print (os.path.dirname(fp))
    # print (sample_dir)

    basename = os.path.basename(line)
    # TODO
    # or basename.split for '.', '_' or both
    bc = basename.split('.', 1)[0]
    # print (os.path.basename(fp))
    # print (bc)

    print (bc, sample_dir, basename, line, sep='\t')
