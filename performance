    
import numpy as np
import matplotlib.pyplot as plt


#--------------------------------
'''
performance

''''

def evaluate(pred,real):  
    tp=0
    tn=0
    fp=0
    fn=0
    for i in range(len(pred)):
        if pred[i]==0:
            if real[i]==1:
                fp+=1
            else:
                tp+=1
        else:
            if real[i]==1:
                tn+=1
            else:
                fn+=1
    accuracy=round((tp+tn)/(tn+tp+fn+fp),3)
    precision=round(tp/(tp+fp),3)
    recall=round(tp/(tp+fn),3)
    mcc=round((tp*tn-fp*fn)/((tp+fp)*(tp+fn)*(tn+fp)*(tn+fn))**(1/2),3)
    f1=round((2*(precision*recall)/(precision+recall)),3)
    return accuracy,precision,recall,mcc,f1
    
#----------------------------------------------------------------------
'''
bar chart

'''
def plot_npy(fname):
    y=np.load(fname)[15000:25000]
    x=range(-int((len(y))/2)+1200,int((len(y))/2)+1200)
    plt.bar(x,y)
    plt.show()
    
#--------------------------------------------------------------------------
'''
table
'''
allp=[]
allr=[]
allf=[]
for i in range(1,6):
    precisions=[]
    recalls=[]
    f1s=[]
    accuracy,precision,recall,mcc,f1=evaluate(pred=np.load("models/ver6/pred_"+str(i)+"_nonTATA.npy"),\
                                                   real=np.load("nonTATAlabels/nT"+str(i)+"labels.npy"))
    allp.append(precision);allr.append(recall);allf.append(f1)
table_allp = pd.DataFrame(allp, columns=["model predict"],
                          index=["mouse", "shrew", "rat", "rabbit","human"])
table_allr = pd.DataFrame(allr, columns=["model predict"],
                          index=["mouse", "shrew", "rat", "rabbit","human"])
table_allf = pd.DataFrame(allf, columns=["model predict"],
                          index=["mouse", "shrew", "rat", "rabbit","human"])    
    
    
    
    
