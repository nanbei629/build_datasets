# -- coding: utf-8 --
from sklearn import datasets
import  numpy as np
from PIL import Image
import os
import csv
import skimage

#读取文件夹中的图像信息，生成列表
def generate_dataset(path):
    filelist = os.listdir(path)
    csvfile = open("imgfile.txt", 'w')
    for files in filelist:
        filename = os.path.splitext(files)[0]
        str1 = path + files + ' ' + filename[0] + '\n'
        csvfile.writelines(str1)
    csvfile.close()
    return csvfile.name

#生成sklearn训练数据集
def load_imgesets(filename):
    file = open(filename,'r')
    data = []
    target = []
    data = np.array(data,dtype=float)
    flag = 1
    for line in file:
        # 分割图像路径与类别
        str = line.split(' ',1)
        #读取图片转换为灰度图
        #将灰度矩阵转换为一维数据
        if flag == 1:
            flag = 0
            data = np.array(Image.open(str[0]).convert('L')).reshape(1,-1)
        else:
            row = np.array(Image.open(str[0]).convert('L')).reshape(1, -1)
            data = np.row_stack((data, row))
        target.append(str[1])
    file.close()
    target =np.asarray(target,dtype=int)
    return data,target

def image_datasets(path):
    filename = generate_dataset(path)
    data,target = load_imgesets(filename)
    return data,target
