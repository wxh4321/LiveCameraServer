#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/15 14:02
# @Author  : wxh
# @Site    : 
# @File    : actionutils.py
# @Software: PyCharm
import json
import utils.tools.removetagfile as removetagfile
path = "./proxyfile/dic/video.json"
path1 = "./tmpvideo"
def checkWord(str='',label='',path='./proxyfile/dic/video.json'):#如果存在，不再保存，返回value；否则返回nodata
    result = 'nodata'
    # 读取数据
    data = {}  # 存放读取的数据
    with open(path, 'r', encoding='utf-8') as rjson_file:
        data = json.load(rjson_file)
        for key, value in data.items():
            if key == str:
                return value
    with open(path, 'w', encoding='utf-8') as wjson_file:
        data[str] = label
        json.dump(data, wjson_file)
    return result

def clearBaiTtsFile():
    remove_list = []
    retain_list = []
    # remove_list = ['80271579073479.93832547700.wav', 'a.txt', 'b.txt']  # 要删除的文件名称
    # retain_list = ['c.txt']  # 要保留的文件名称

    # 读取数据
    data = {}  # 存放读取的数据
    with open(path, 'r', encoding='utf-8') as rjson_file:
        data = json.load(rjson_file)
        if data:
            for key, value in data.items():
                remove_list.append(value+'.wav')

    ##清空录音文件
    rtf = removetagfile.RemoveTagFile()
    rtf.removeFile(path1, remove_list, retain_list)
    ##清空json文件
    with open(path, 'w', encoding='utf-8') as wjson_file:
        json.dump({}, wjson_file)
def clearVideoFile():
    remove_list = []
    retain_list = []
    # 读取数据
    data = {}  # 存放读取的数据
    with open(path, 'r', encoding='utf-8') as rjson_file:
        data = json.load(rjson_file)
        if data:
            for key, value in data.items():
                remove_list.append(value+'.webm')

    ##清空录音文件
    rtf = removetagfile.RemoveTagFile()
    rtf.removeFile(path1, remove_list, retain_list)
    ##清空json文件
    with open(path, 'w', encoding='utf-8') as wjson_file:
        json.dump({}, wjson_file)

if __name__=='__main__':
    print(checkWord('hello2','good2'))
    clearBaiTtsFile()