import os
import numpy as np
import matplotlib.pyplot as plt

file_name_list = []
coor=[]
file_path='E:/cszdata/WXWork/1688850447514390/Cache/File/2022-02/gyy.txt'
with open(file_path, 'r') as file_to_read:
    while True:
        lines = file_to_read.readline().strip()  # 整行读取数据
        if not lines:
            break
            pass
        file_name_list.append(lines)
        pass

for i in range(len(file_name_list)):
    line=file_name_list[i].split('"')
    line_coor=[line[1],line[5],line[7]]
    #line_coor=np.array(line_coor,dtype='')
    coor.append(line_coor)
coor=np.array(coor,dtype='double')

#
# coor[:,1]=np.argsort(coor[:,1])
# coor[:,2]=np.argsort(coor[:,2])
#coor=np.array(coor,dtype='int')
plt.scatter(coor[0:2226,1],coor[0:2226,2]*(-1),marker='.')
for i in range(2227):
    plt.text(coor[i][1],coor[i][2]*(-1),int(coor[i][0]),fontsize=8)
plt.show()
print(coor)