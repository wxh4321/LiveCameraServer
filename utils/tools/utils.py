#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2020/2/6 17:25
#@Author  : wangx 
#@FileName: utils.py
#@Software: PyCharm
import os
import time

def getFileSize(path):
    bsize = os.path.getsize(path)
    return float(bsize/(1024*1024))
def getFileListName(filepath="../../tmpvideo"):
    res = []
    list = os.listdir(filepath)
    for filename in list:
        res.append(filename.split(".")[0])
    return res
def mkdir(path):#根据时间创建文件夹
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
        print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 目录已存在')
        return False

if __name__=='__main__':
    print(getFileSize("./utils.py"))
    print(getFileListName())
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    # 定义要创建的目录
    mkpath = "../../tmpvideo/test"
    # 调用函数
    mkdir(mkpath)