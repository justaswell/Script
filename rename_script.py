import os

#file='E:/soma_seg/data.txt'
mode='seg'
data_path='E:/soma_seg/'

if mode=='crop':
    files=os.listdir(data_path+'data')
elif mode=='seg':
    files = os.listdir(data_path + 'label')
#print(files)
for file in files:
    _,name=os.path.split(file)
    #print(name)
    begin=name.find("_")
    if mode=='crop':
        end=name.find('_crop.tiff')
    elif mode=='seg':
        end = name.find('.tiff')
    brainID=name[0:begin]
    if mode=='crop':
        somaID=name[begin+1:end]
    elif mode=='seg':
        somaID = name[begin + 5:end]
    print(brainID)
    print(somaID)
    if mode=='crop':
        os.rename(data_path + 'data/' + name, data_path + 'data/' + 'Imgsoma_' + brainID + '_' + somaID + '.tiff')
    elif mode=='seg':
        os.rename(data_path+'label/'+name,data_path+'label/'+'seg_Imgsoma_'+brainID+'_'+somaID+'.tiff')
    #print(begin)
'''data_path='D:/A_DLcsz/correct/'
filename='raw2/fixed_data/label'
files=os.listdir(data_path+filename)
for file in files:
    _, name = os.path.split(file)
    os.rename(data_path +filename+ '/' + name, data_path +filename+ '/'+'seg_'+name)'''

