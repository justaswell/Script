import os

file_name_list1 = []
file_name_list2 = []
file_path1='D:/A_DLcsz/resizetrain/val_name_list.txt'
file_path2='D:/A_DLcsz/resizetrain/train_name_list.txt'

with open(file_path1, 'r') as file_to_read:
    while True:
        lines = file_to_read.readline().strip()  # 整行读取数据
        if not lines:
            break
            pass
        file_name_list1.append(lines)
        pass
with open(file_path2, 'r') as file_to_read:
    while True:
        lines = file_to_read.readline().strip()  # 整行读取数据
        if not lines:
            break
            pass
        file_name_list2.append(lines)
        pass
print(len(file_name_list1))
print(len(file_name_list2))
for name in file_name_list1:
    #print(name)
    if 'rdflip-'+name in file_name_list2:
        file_name_list2.remove(name)
print(len(file_name_list2))

f = open(file_path2, 'w')
for i in range(len(file_name_list2)):
    f.write(str(file_name_list2[i]) + "\n")
f.close()