#!/usr/bin/python2

import sys  #one can use argparse for versatile function of argument parsing
import string

#parsing commandline arguments
genome_file, gene_table, output = sys.argv[1:]

#store genome sequence into a single string
genome = ""
with open(genome_file) as GENOME:
    for seq in GENOME:
        if seq.find(">") != 0: #skip the header of the genome fa file
            genome += seq.strip() #concatenate genome sequences into a 0-indexing string

#define a function for reverse complement for later usage
def reverse_complement(sequence):
    '''
    using the build in string translation method and helper function maketrans to
    generate the reverse complement of the input sequence
    '''
    intab = "ATCGatcgN" #including mask and ambiguous nuclear acids
    outtab = "TAGCtagcN"
    trantab = string.maketrans(intab, outtab)  #creat an object for translation rules
    return sequence.translate(trantab)[::-1]  #specifying -1 as step for string slicing to return reversed sequence



#extract gene sequence and print output
#read genes from gene table and write it out one by one without creat a dict to store
#the gene table
with open(output,'w') as OUTPUT:
    with open(gene_table) as GENETABLE:
        for gene in GENETABLE:
            if gene.find("#") == 0: continue
            start, stop, strand, gend_id, locus, locus_tag, protein_accession = gene.strip().split()[2:9]
            #extract raw sequence from genome
            gene_sequence = genome[int(start)-1:int(stop)] #gene table coordinates are 1-indexing
            #check reverse complement
            if strand == "-":
                gene_sequence = reverse_complement(gene_sequence) #call the function

            #parsing the gene information and sequence to print out
            OUTPUT.write(locus_tag+"\t"+gene_sequence+"\n")
