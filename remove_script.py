import glob
import os

file_path='D:/A_DLcsz/resizetrain/val_name_list.txt'
file_name_list=[]
with open(file_path, 'r') as file_to_read:
    while True:
        lines = file_to_read.readline().strip()  # 整行读取数据
        if not lines:
            break
            pass
        file_name_list.append(lines)
        pass
print(len(file_name_list))

files=glob.glob('D:/A_DLcsz/resizetrain/all/data/*')
#print(files)

for name in file_name_list:
    if 'D:/A_DLcsz/resizetrain/all/data\\'+name in files:
        #count+=1
        os.remove('D:/A_DLcsz/resizetrain/all/data/'+name)
        os.remove('D:/A_DLcsz/resizetrain/all/label/' + 'seg_'+name)
