#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/1 21:11
# @Author  : wxh
# @Site    : 
# @File    : Server.py
# @Software: PyCharm
#7天缓存，最小储存空间73G

import utils.webutils as webtools
import utils.tools.utils as utils
import time
import datetime
from flask import jsonify
from flask import Flask, render_template, request,Response,make_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)

ip = webtools.getLocalIP() #获取本地ip
hasfile = False
blobfile= {}
#显示所有文件夹
@app.route('/',methods=['GET','POST'])
def welcome():
    if request.method == 'GET':
            return render_template('welcome.html')

@app.route('/web/live/',methods=['GET','POST'])
def getWebLive():
    global blobfile
    timeStr = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    global hasfile
    if request.method =='GET':
        return render_template('welcome.html')
    if request.method=='POST':
        if not hasfile:
            utils.mkdir("./tmpvideo/" + timeStr)
            hasfile = True
        # 打印时间戳
        # print(time.time())
        file_name = request.form["cameraid"]
        reqfile = request.files["streamer"].stream.read()
        blobfile[file_name] = request.files["streamer"]
        with open("./tmpvideo/"+ timeStr+"/" + file_name + ".mkv", "ab+") as file:  # 保存视频文件
            if reqfile:
                file.write(reqfile)
                return jsonify({"code":200,"result":"ok"})
        file.close()
        return jsonify({"code":201,"result":"error"})

@app.route('/web/liveurl/',methods=['GET','POST'])
def getWebLiveUrlList():
    today = datetime.date.today()
    yesterday = str(today - datetime.timedelta(days=1))
    timeStr = yesterday
    if request.method =='POST':
        return render_template('welcome.html')
    if request.method=='GET':
        data = []
        filenamelist = utils.getFileListName("./tmpvideo/"+timeStr)
        for  filename in filenamelist:
            data.append("https://" + ip + ":30800/web/video/" + filename)
        return jsonify({"code":200,"list":data})

@app.route('/web/video/<file_key>',methods=['GET','POST'])
def getWebVideoStream(file_key):
    today = datetime.date.today()
    yesterday = str(today - datetime.timedelta(days=1))
    timeStr = yesterday
    if request.method=='GET':
        def generate():
            path = './tmpvideo/'+timeStr+'/'+file_key+'.mkv'
            with open(path, 'rb') as fvideo:
                data = fvideo.read(1024)
                while data:
                    yield data
                    data = fvideo.read(1024)
        return Response(generate(), mimetype="video/x-matroska")

    if request.method =='POST':
        return render_template('welcome.html')
@app.route('/web/blobfileurl/',methods=['GET','POST'])
def getBlobFileList():
    timeStr = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    if request.method =='POST':
        return render_template('welcome.html')
    if request.method=='GET':
        data = []
        filenamelist = utils.getFileListName("./tmpvideo/"+timeStr)
        for  filename in filenamelist:
            data.append("https://" + ip + ":30800/web/getBlobFile/" + filename)
        return jsonify({"code":200,"list":data})

@app.route('/web/getBlobFile/<file_key>',methods=['GET','POST'])  #7.4168
def getBlobFileStream(file_key):
    if request.method=='GET':
        def generate():
            fvideo = blobfile[file_key]
            data = fvideo.read(1024)
            while data:
                yield data
                data = fvideo.read(1024)
        return Response(generate(), mimetype="video/x-matroska")
    if request.method =='POST':
        return render_template('welcome.html')


if __name__ == '__main__':
    sslpath="./ssl/"
    #port为端口，host值为0.0.0.0即不单单只能在127.0.0.1访问，外网也能访问
    app.run(host='0.0.0.0',port='30800',ssl_context=(sslpath+'certificate.pem', sslpath+'privatekey.pem'))

