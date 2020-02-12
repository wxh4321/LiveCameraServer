#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/11 15:58
# @Author  : wxh
# @Site    : 
# @File    : requestWeb.py
# @Software: PyCharm
import utils.actionutils as action
import utils.tools.utils as utils

def postWebLiveVideo(params,arr):
    if params.get('remake'):#重新构造文件
       action.clearVideoFile()
    fileSize = utils.getFileSize(arr[1])
    if fileSize>10:
        print("file size : "+str(fileSize)+" M")
    file_name = arr[0]
    data = {
        'cameraid': '',
        'streamer':''
    }
    for key, value in data.items():
        data[key] = params.get(key)
    response = {'code':200,'content':file_name,'stream':data['streamer']}
    return response


if __name__=="__main__":
    action.clearVideoFile()