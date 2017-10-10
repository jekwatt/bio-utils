#! /usr/bin/env python3

import sys

basecomplement = {'G': 'C', 'A': 'T', 'T': 'A', 'C': 'G', 'N': 'N',
                      'g': 'c', 'a': 't', 't': 'a', 'c': 'g', 'n': 'n'}

for line in sys.stdin:
    data = line.strip().split('\t')
    # sequence = data[0].lower()
    sequence = data[0]
    letters = list(sequence)
    letters = [basecomplement[base] for base in letters]
    # return ''.join(letters)
    comp_dna = ''.join(letters)
    rev_comp_dna = comp_dna[::-1]
    output = data + [str(rev_comp_dna)]
    print(*output, sep='\t')
