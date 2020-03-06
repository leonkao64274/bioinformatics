from tqdm import tqdm
import numpy as np
#---------------------------------------------------------------------
'''
get gene name, location, geneid from a GFF file

'''
def load_genes(x="../../rat/GCF_000001895.5_Rnor_6.0_genomic.gff"):
    with open(x,"r") as f:
        gff=f.readlines()
    gff=[sublist.split("\t") for sublist in gff if sublist[0]!="#"]
    genes=[sublist for sublist in gff if sublist[2]=="gene" and sublist[6]=="+"]
    genes=[[sublist[0],sublist[3],sublist[4],sublist[8]] for sublist in genes]
    descriptions=[sublist[-1].split(";")[1].split(",")[0].split(":")[1] for sublist in genes ]
    genes=[[genes[i][0],genes[i][1],genes[i][2],descriptions[i]] for i in range(len(genes))]
    return genes
 
 
 
 #----------------------------------------------------------------------
 '''
 load a fasta file and make it into a dictionary
 
 '''
 def load_fasta(x="../../rat/GCF_000001895.5_Rnor_6.0_genomic.fna"):
    with open (x,"r") as f:
        fastafile=f.readlines()
    gene_names=[name.split()[0].lstrip(">") for name in fastafile if name[0]==">"]
    fasta=[]
    tmpDNA=""
    for line in tqdm(fastafile):
        if line[0]==">":
            fasta.append(tmpDNA)
            tmpDNA=""
        else:
            tmpDNA+=line.upper().rstrip()
    fasta.append(tmpDNA)
    del(fasta[0])
    dict_fasta={}
    for i in range(len(gene_names)):
        dict_fasta.update({gene_names[i]:fasta[i]})
    return dict_fasta
    
    
    
 #------------------------------------------------------------------------------------
 '''
 arraylize sequences
 
 '''
 
 def convert_sequences_to_array(sequences):
    '''
    inputs: sequence of nucleotides represented as a string composed of A, C, G, T
    outputs: a list of numpy array representations of a sequence with:
             A = [1, 0, 0, 0]
             C = [0, 1, 0, 0]
             G = [0, 0, 1, 0]
             T = [0, 0, 0, 1]
             
    '''

    nucleotide_array_dict = {'A': [1, 0, 0, 0],
                             'C': [0, 1, 0, 0],
                             'G': [0, 0, 1, 0],
                             'T': [0, 0, 0, 1],
                             'N': [0.25,0.25,0.25,0.25],
                             'R':[0.5,0,0.5,0],
                             'Y':[0,0.5,0,0.5],
                             'M':[0.5,0.5,0,0],
                             'K':[0,0,0.5,0.5],
                             'S':[0,0.5,0.5,0],
                             'W':[0.5,0,0,0.5],
                             'B':[0,0.33,0.33,0.33],
                             'D':[0.33,0,0.33,0.33],
                             'H':[0.33,0.33,0,0.33],
                             'V':[0.33,0.33,0.33,0]}
    
    sequence_array_list = []
    for seq in sequences:
        seq_array = []
        for nuc in seq:
            seq_array.append(nucleotide_array_dict[nuc])
        seq_array = np.array(seq_array) 
        sequence_array_list.append(seq_array)
    return sequence_array_list
    
    
