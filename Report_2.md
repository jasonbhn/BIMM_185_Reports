
# Report 2

```
This week we did 3 main mini projects using Python and Bash.
```
## zscore.sh
```
The first thing we did is traversing through a complex directory and extract information z-score and protein name from the file in the innermost directory. 
The script is stored in zscore.sh
This is a good demonstration of the use of regex and pipelining. 
Traversal through files could be very important. 
This traversal could also be used to make table, like a csv file where you grab a locus tag and protein name and some coordinates and put them in one file. You can also grab the conserved regions across multiple genomes. And you can generate a file for blast or similarity test. 
The code could also be used to extract some files from a folder and concatenate to generate a report. Such as the case here, where we would, instead of grabing the info in report file, take report file as a whole and concatenate the report one after another. Maybe by passing this into a mathematical program, we can generate statistics of the genomes or genes. 

```
## GeneSequenceExtract2.py, my_gene_extractions.py
```
For some reasons, My reverse lambda function does not work properly,I think I might need some help to get that dealt with. 
So, here for instructional clarity, I used the python file provided by class resources. 
This is a program that grabs the gene from the genome file and concatenate after the locus tag separated by a tab. The program will reverse the reverse strand so that all gene sequence are forward directioned. 
This program is very versatile, you can modify the targeted sequence that you are looking for, this involves modifying the regular expression that is used to grab the entire gene sequence. Maybe, we are just trying to grab a specific sequence that CRISPER-CAS9 will be able to make a cut. So you can find out if these gene can be edited with the given cas9 recognition sequence. 
Or, instead of searching in a gene, you do data mining in a genome file, and try to extract conserved region of a certain primer or promoter binding site, and you want to know the similarity score between each site. 
Or, more general example would be 16srDNA, where for the most part they are highly conserved except for some crucial regions that could differentiate one species of bacteria from another. But these are all pre-processing, to really do them, we might need to use NCBI BLAST and similar tools, such as AntiSMASH.

```
## table.py
```
This is a continuation of the gene_sequence_extraction program. Once the output are generated from previous program, it will serve as the input to this table.py, where it generates an output of tabular separated values. And each row start with locus tag and then the frequency of the appearance of a specific codon in the gene sequence. The program make used of the wrapper function where the separated sequence are sliced into triplets. 
To cleverly make use of the function, we can in fact do file conversions from a gene nucleotide sequence to codon sequence. Where you can match the degenerated codon sequence with the codon and concatenate the codon letter to the string of amino acid sequence. 

```
## NCBI database
```
NCBI database provides us with ample amount of free and to-some-degree reliable information about organism's protein, genome, metabolic networks and so on so forth. 
Below are some useful informations:
Main website: https://www.ncbi.nlm.nih.gov/
Blast+ suite of programs:  ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/
Preformatted BLAST databases: ftp://ftp.ncbi.nlm.nih.gov/blast/db/
General FTP site: ftp://ftp.ncbi.nlm.nih.gov/

You can also get the whole genome by accessing the species code and name. 


```
