#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2020/2/9 22:06
#@Author  : wangx 
#@FileName: WebSocketServer.py
#@Software: PyCharm
from flask import Flask, render_template, request,Response,make_response
from flask_cors import CORS
from geventwebsocket.websocket import WebSocket,WebSocketError
from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer
import json
import ssl
import requests
# ssl._create_default_https_context = ssl._create_unverified_context
requests.packages.urllib3.disable_warnings()

app = Flask(__name__)
# CORS(app, supports_credentials=True)
user_socket_dict={}

###由于证书问题目前不能用
#socket服务
@app.route('/ws/<username>')
def ws(username):
    user_socket=request.environ.get("wsgi.websocket")
    if not user_socket:
        return "请以WEBSOCKET方式连接"
    user_socket_dict[username]=user_socket
    print(user_socket_dict)
    while True:
        try:
            user_msg = user_socket.receive()
            for user_name,u_socket in user_socket_dict.items():
                who_send_msg={
                    "send_user":username,
                    "send_msg":user_msg
                }

                if user_socket == u_socket:
                    continue
                u_socket.send(json.dumps(who_send_msg))

        except WebSocketError as e:
            user_socket_dict.pop(username)
            print(user_socket_dict)
            print(e)


if __name__ == '__main__':
    sslpath="./ssl/"
    keyfile = sslpath + 'privatekey.pem',
    certfile = sslpath + 'certificate.pem'
    # 生成SSL上下文
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    # 加载服务器所用证书和私钥
    context.load_cert_chain(certfile,sslpath + 'privatekey.pem')
    context.verify_mode = ssl.CERT_NONE
    #port为端口，host值为0.0.0.0即不单单只能在127.0.0.1访问，外网也能访问
    # app.run(host='0.0.0.0',port='30800',ssl_context=(sslpath+'certificate.pem', sslpath+'privatekey.pem'))
    http_serve = WSGIServer(("0.0.0.0", 8008), app,handler_class=WebSocketHandler,ssl_context=context)
    http_serve.serve_forever()
