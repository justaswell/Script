import pandas as pd
import numpy as np

brainID='236174'
file="E:/soma_seg/"+brainID+"_crop_redo2Rreplot/label_CSZ.csv"
infile='E:/soma_seg/'+brainID+'.csv'
data=pd.read_csv(file)
data=np.array(data)
newdata=[]
print(data.shape)
x,_=data.shape
for i in range(x):
    #print(data[i][1])
    #item=data[i]
    label=data[i][1]
    if label!=1:
        #print(data[i])
        newdata.append(data[i][0])
print(newdata)
newdata=pd.DataFrame(newdata)
newdata.to_csv(infile)

