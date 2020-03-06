import random
def get_TSS_nonTSS(gff_name,fasta_name):   
    rdata=[]
    comment=[]
    delnum=0
    with open(gff_name,"r") as f:
        rdata=f.readlines()
    for i in range(9):
        del(rdata[0])
    for i in range(len(rdata)):
        if rdata[i][0]=="#":
            comment.append(i)
        rdata[i]=rdata[i].split()
    for i in range(len(comment)):
        del(rdata[comment[i]-delnum])
        delnum+=1
    isgene=[]
    for i in range(len(rdata)):
        if rdata[i][2]=="gene":
            isgene.append(rdata[i])
    typelist=[]
    for i in range(len(rdata)):
        if rdata[i][2] not in typelist:
            typelist.append(rdata[i][2])
    genetrandp=[]
    genetrandn=[]
    genetrandun=[]
    for i in range (len(isgene)):
        if isgene[i][6]=="+":
            genetrandp.append([isgene[i][0],isgene[i][3],isgene[i][4],isgene[i][6]])
        elif isgene[i][6]=="-":
            genetrandn.append([isgene[i][0],isgene[i][3],isgene[i][4],isgene[i][6]])
        else:
            genetrandun.append([isgene[i][0],isgene[i][3],isgene[i][4],isgene[i][6]])

    TSSlocation=[]

    for i in range(len(genetrandp)):
        TSSlocation.append([genetrandp[i][0],int(genetrandp[i][1])-50,int(genetrandp[i][1])+200])
    rfasta=[]
    fasta2=[]
    genename=[]
    string=""
    with open(fasta_name,"r") as f:
        rfasta=f.readlines()
    for i in range(len(rfasta)):
        if rfasta[i][0]==">":
            fasta2.append(string)
            string=""
            genename.append(rfasta[i])
        else:
            string+=rfasta[i].rstrip()
    del(fasta2[0])
    del(genename[-1]) 
    for i in range(len(genename)):
        genename[i]=genename[i].split()[0].lstrip(">")
    genefasta={}
    for i in range(len(genename)):
        genefasta.update({genename[i]:fasta2[i]})
    TSSfasta=[]
    for i in range(len(TSSlocation)):
        if (TSSlocation[i][0] in genefasta.keys()):
            TSSfasta.append(genefasta[TSSlocation[i][0]][TSSlocation[i][1]:TSSlocation[i][2]].upper())
    n=0        
    while(n<len(TSSfasta)):
        while(len(TSSfasta[n])!=250):
            del(TSSfasta[n])
        n+=1
    nonTSSstart=[]
    nonTSSname=[]
    for i in range(50000):
        temp=random.randint(0,len(genetrandp)-1)
        if int(genetrandp[temp][2])-250>int(genetrandp[temp][1]):
            nonTSSname.append(temp)
            nonTSSstart.append(random.randint(int(genetrandp[temp][1]),int(genetrandp[temp][2])-250))
    nonTSSfasta=[]           
    for i in range(len(nonTSSname)):
        if  genetrandp[nonTSSname[i]][0] in genefasta.keys():
            name=genetrandp[nonTSSname[i]][0]
            nonTSSfasta.append(genefasta[name][nonTSSstart[i]:nonTSSstart[i]+250].upper())
    TATA_TSSfasta=[]
    TATA_nonTSSfasta=[]
    for i in range(len(TSSfasta)):
        for j in range(45):
            if TSSfasta[i][j:j+4]=="TATA":
                TATA_TSSfasta.append(TSSfasta[i])
    for i in range(len(nonTSSfasta)):
        for j in range(45):
            if nonTSSfasta[i][j:j+4]=="TATA":
                TATA_nonTSSfasta.append(nonTSSfasta[i])
    nonTATA_TSSfasta=[]
    nonTATA_nonTSSfasta=[]
    for i in range(len(TSSfasta)):
        if TSSfasta[i] not in TATA_TSSfasta:
            nonTATA_TSSfasta.append(TSSfasta[i])
    for i in range(len(nonTSSfasta)):
        if nonTSSfasta[i] not in TATA_nonTSSfasta:
            nonTATA_nonTSSfasta.append(nonTSSfasta[i])
    print(len(nonTATA_nonTSSfasta))
    TATA_TSSinput=np.array(convert_sequences_to_array(TATA_TSSfasta))
    nonTATA_TSSinput=np.array(convert_sequences_to_array(nonTATA_TSSfasta))
    TATA_nonTSSinput=np.array(convert_sequences_to_array(TATA_nonTSSfasta))
    nonTATA_nonTSSinput=np.array(convert_sequences_to_array(nonTATA_nonTSSfasta))
    return TATA_TSSinput,nonTATA_TSSinput,TATA_nonTSSinput,nonTATA_nonTSSinput
