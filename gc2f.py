#!/usr/bin/env python3

import sys

for line in sys.stdin:
    data = line.strip().split('\t')
    sequence = data[0].lower()
    num_c = sequence.count('c')
    num_g = sequence.count('g')
    gc = 100 * (num_c + num_g) / len(sequence)
    gc2f = "%.2f" % gc
    output = data + [str(gc2f)]
    print(*output, sep='\t')
