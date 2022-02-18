import pandas as pd
import numpy as np

brainID='18454'
mode='seg'
file="E:/soma_seg/"+brainID+".csv"
if mode=='crop':
    infile = 'E:/soma_seg/' + brainID + '.txt'
elif mode=='seg':
    infile='E:/soma_seg/'+brainID+'_seg.txt'
#infile='E:/soma_seg/236174.csv'
data=pd.read_csv(file)
data=np.array(data)
(x,_)=data.shape
f = open(infile, 'w')


for i in range(x):
    item=data[i][1]
    begin=item.find('_review_')
    end=item.find('.tiff')
    somaID=item[begin+8:end]
    if mode=='crop':
        f.write(brainID+'_'+somaID+'_crop.tiff' + "\n")
    elif mode=='seg':
        f.write(brainID + '_seg_' + somaID + '.tiff' + "\n")

f.close()

