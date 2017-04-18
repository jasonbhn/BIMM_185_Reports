import sys,os,csv
import fileinput as fi

def readFile():

        file = open('GCF_000005845.2_ASM584v2_genomic.fna','r+')
        txtSch = input("\n")
        txtRplce = input("")

        for line in file:
                file.write( line.replace( txtSch, txtRplce ) )



        proteins = defaultdict(list)

        for line in contents:

                info = line.split('\t')

                ID = info[0]
                ID2 = (infor[1],info[2],info[3].replace('\n',''));

                #add to dictionary

                proteins[ID].append(ID2)

        return proteins

def findBest(proteins):

        for key in proteins:
                best = sorted(proteins[key],key=lambda x: x[1], reverse)[0]
