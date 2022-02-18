import os
import shutil


brainID='236174'
cropfile='E:/BaiduNetdiskDownload/soma_img_crop_uint8/'+brainID+'_img_crop_uint8/'
segfile='E:/soma_seg/'+brainID+'_crop_seg/'
cfile='E:/soma_seg/'+brainID+'.txt'
sfile='E:/soma_seg/'+brainID+'_seg.txt'
datafile='E:/soma_seg/'+brainID+'/data'
labelfile='E:/soma_seg/'+brainID+'/label'

if not os.path.exists(datafile):  # 创建保存目录
    os.makedirs(datafile)
if not os.path.exists(labelfile):  # 创建保存目录
    os.makedirs(labelfile)

filenames_crop=set()
filenames_seg=set()
with open(cfile) as crop_read_file:
    contents0=crop_read_file.readlines()
    for content0 in contents0:
        filenames_crop.add(content0.strip('\n'))

with open(sfile) as seg_read_file:
    contents1=seg_read_file.readlines()
    for content1 in contents1:
        filenames_seg.add(content1.strip('\n'))

for each in os.listdir(cropfile):
    if each in filenames_crop:
        each_path=cropfile+each
        shutil.copy(each_path,datafile)

for each in os.listdir(segfile):
    if each in filenames_seg:
        each_path=segfile+each
        shutil.copy(each_path,labelfile)

