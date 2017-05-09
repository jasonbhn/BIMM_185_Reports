import Bio
import os
import MySQLdb
import gzip
script, genbank = argv
#server = MySQLdb.open_database(driver="MySQLdb", user="b2ni",
#                     passwd = "", host = "bm185s-mysql.ucsd.edu", db="b2ni_db")
#db=_mysql.connect(host="bm185s-mysql",user="b2ni",
                  passwd="Jason926",db="b2ni_db")
#cursor = db.cursor()
#add_genome = ("INSERT INTO genomes "
#            "(genome_id, name, tax_id, domain, num_replicons)")
cntCDS=0
cntReplicons=0

cntGenome=0

def split_at(s, c, n):
    words = s.split(c)
    return c.join(words[:n]), c.join(words[n:])

def take_genbank():
    cntGenome = cntGenome+1
    gnmReplicons= 0
    gnmSize = 0
    gnmCDS=0
    input_handle = gzip.open('%s'%genbank, "rU")
    outgnm = open("genomes.txt","w")
    outgne = open("genes.txt","w")
    outrpln = open("replicons.txt","w")
    outfunc = open("functions.txt","w")
    outxref = open("gene_xrefs.txt","w")
    outexn = open("exons.txt","w")
    outsynm = open("gene_synonym.txt","w")


    for record in SeqIO.parse(input_handle, "genbank"):
        cntReplicons++
        gnmReplicons++
        accession = record.name
        descri = record.description
        replicon_structure = record.annotations['topology']
        date = record.annotations['date']
        domains = record.annotations['taxonomy']
        domain = domains[0]
        ssize = record.annotations['contig'].partition("..")
        size = int(ssize[2])
        gnmSize+=size
        assem=(os.path.basename(genbank)).split('_')
        assembly = assem[0]+'_'+assem[1]
        names = descri.split(',')
        replicon_name = names[0]
        if(names[1]==" complete genome."):
            replicon_type = "chromosome"
        else:
            replicon_type = "plasmid"
        genome_name = record.annotations['source']


        for feature in record.features:
            if(feature.type == 'source'):

                a = feature.qualifiers.get('db_xref')[0]
                aa =a.partition(':')
                tax_id = aa[2]
            if(feature.type == 'CDS'):
                #this is gene_id
                cntCDS++
                gnmCDS++
                #strand
                str1 = str(feature.location)
                strand = '+'
                if(str1.find('+')):
                    strand = 'F'
                else:
                    strand = 'R'
                itera = str1.count(':')
                ses =re.findall('\d+',refs)
                i = 0
                cds_start = ses[0]
                cds_end = ses[itera*2]
                gene_length = cds_end - cds_start
                while(i < itera*2):
                    exon_start = ses[i]
                    exon_end = ses[i+1]
                    i = i+2
                    length_exon = exon_end - exon_start
                #exon_start = int(str1.start)
                #exon_end = int(str1.end)
                #length_exon = exon_end - exon_start
                    outexn.write(cntCDS+'\t'+itera+'\t'+exon_start+'\t'+exon_end+'\t'+length_exon)

                gene_name = feature.qualifiers.get('gene')[0]
                outsynm.write(cntCDS+'\t'+gene_name)

                str2 = feature.qualifiers.get('locus_tag')[0]
                locus_tag = str2

                str3 = feature.qualifiers.get('gene_synonym')[0]
                gene_synonym = str3
                outsynm.write(cntCDS+'\t'+gene_synonym)

                str4 = feature.qualifiers.get('function')[0]
                function = str4
                outfunc.write(cntCDS+'\t'+function)

                str5 = feature.qualifiers.get('product')[0]
                product = str5

                str6 = feature.qualifiers.get('protein_id')[0]
                protein_id = str6
                #create a row in out handle xref with protein_id, gene_id, db as "NCBI"
                outxref.write(cntCDS+'\t'+"NCBI"+'\t'+protein_id)
                refs = feature.qualifiers.get('db_xref')

                for str7 in refs:
                    db_id = str7.partition(":")
                    xdb = db_id[0]
                    xid = db_id[2]
                    #in out_handle xref, write a row with the given gene_id
                    #db and ID
                    outxref.write(cntCDS+'\t'+xdb+'\t'+xid)

                #write table of gene
                outgne.write(cntGenome+'\t'+cntReplicons+'\t'+cntCDS+'\t'+locus_tag+'\t'+protein_id+'\t'+gene_name+'\t'+strand+'\t'+itera+'\t'+gene_length+'\t'+product)

            #write table of replicons outside of that.
            outrpln.write(cntCDS+'\t'+cntGenome+'\t'+replicon_name+'\t'+replicon_type+'\t'+replicon_structure+'\t'+gnmCDS+'\t'+size+'\t'+accession+'\t'+date)
        #write table of genomes
        outgnm.write(cntGenome+'\t'+genome_name+'\t'+tax_id+'\t'+domain+'\t'+gnmReplicons+'\t'+gnmCDS+'\t'+gnmSize+'\t'+assembly)
    outexn.close()
    outgne.close()
    outgnm.close()
    outfunc.close()
    outsynm.close()
    outxref.close()
    outrpln.close()


take_genbank()




#server.commit()
