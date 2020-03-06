import numpy as np
#-----------------------------------------
'''
get ortho geneID form ortho database

'''
def load_ortho(x="ortho/rmh_r_geneid.txt"):
    with open(x,"r") as f:
        geneids=f.readlines()
    ortho_geneids=[geneid.rstrip() for geneid in geneids]
    return ortho_geneids
#----------------------------------------------------------------------
'''
get the ortho_gropuID
x:taxID

'''
def gene2og(x="9606"):
    rdata2=[]
    with open ("odb10v1_OG2genes.tab","r") as f:
        rdata2=f.readlines()
    ogs=[line.split("\t")[0] for line in tqdm(rdata2)]
    orthoids_2=[line.split("\t")[1] for line in tqdm(rdata2)]
    ogs_orthoids=[[ogs[i],orthoids_2[i].rstrip()] for i in tqdm(range(len(orthoids_2))) if orthoids_2[i][0:4]==x]

    return ogs_orthoids




    
  
