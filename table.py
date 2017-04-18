#!/usr/bin/python2
#for report 2.
import sys  #one can use argparse for versatile function of argument parsing
import string
from collections import Counter
import textwrap
#parsing commandline arguments, takes in an input file name and an output file name. 
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
#create an empty array list that stores the problematic genes.
shift = []
#open the file to edit
with open(output,'w') as OUTPUT:
    #open the input file as list of lines
    file = open(locus_seq)
    ltabseq = file.readlines()
    #loop through the lines and extract information to put into the output file
    for line in ltabseq:
        # if it is not header, then we can extract info out of it
        if line.find("b")==0:
            #if the sequence is not divisible by 3 then it's errorneous
            line = line.strip()
            lo_seq = line.split('\t')
            if(len(lo_seq[1])%3!=0):
                shift.append(lo_seq[0])
            #else, let's take its locus tag in a string and now start to count codon
            #frequency in the gene
            else:
                row = lo_seq[0]+'\t'
                #this will help split up the gene into triplets
                search_in = textwrap.wrap(lo_seq[1],3)
                #iteratively search and add the frequency into the list
                for codon in codons:
                    row =row + str(search_in.count(codon)) + '\t'
                row = row + str(len(lo_seq[1]))
                OUTPUT.write(row+'\n')
    #add the problematic genes
    OUTPUT.write("Problematic Genes are: ")
    for shif in shift:
        OUTPUT.write(shif+'\n')
