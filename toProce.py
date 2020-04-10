#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

host = "127.0.0.1" #Processingで立ち上げたサーバのIPアドレス
port = 10001       #Processingで設定したポート番号
text = ["ア","イ","ウ","エ","オ"]

if __name__ == '__main__':
    socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #オブジェクトの作成
    socket_client.connect((host, port))                               #サーバに接続

    for x in text:
        socket_client.send(text[x].encode('utf-8')) #データを送信 Python3