#!/usr/bin/python2

import sys  #one can use argparse for versatile function of argument parsing
import string
from collections import Counter
import textwrap
#parsing commandline arguments
locus_seq, output = sys.argv[1:]

#create a dictionary with keys of codons:
codons = ['GCT', 'GCC', 'GCA', 'GCG',
               'TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG',
               'CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG',
               'AAA', 'AAG', 'AAT', 'AAC', 'GAT', 'GAC',
               'TTT', 'TTC', 'TGT', 'TGC', 'CCT', 'CCC', 'CCA', 'CCG',
               'CAA', 'CAG', 'TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC',
               'GAA', 'GAG', 'ACT', 'ACC', 'ACA', 'ACG',
               'GGT', 'GGC', 'GGA', 'GGG', 'CAT', 'CAC', 'TAT', 'TAC',
               'ATT', 'ATC', 'ATA', 'GTT', 'GTC', 'GTA, ''GTG',
               'TAA', 'TGA', 'TAG']
shift = []
with open(output,'w') as OUTPUT:
    file = open(locus_seq)
    ltabseq = file.readlines()
    for line in ltabseq:
        if line.find("b")==0:
            line = line.strip()
            lo_seq = line.split('\t')
            if(len(lo_seq[1])%3!=0):
                shift.append(lo_seq[0])
            else:
                row = lo_seq[0]+'\t'
                search_in = textwrap.wrap(lo_seq[1],3)
                for codon in codons:
                    row =row + str(search_in.count(codon)) + '\t'
                row = row + str(len(lo_seq[1]))
                OUTPUT.write(row+'\n')
    OUTPUT.write("Problematic Genes are: ")
    for shif in shift:
        OUTPUT.write(shif+'\n')
