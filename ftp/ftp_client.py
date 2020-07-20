import os
import sys
from socket import socket
from time import sleep

HOST='124.70.187.114'
PORT=8888
ADDR=(HOST,PORT)
class FTP_Client:
    def __init__(self,sock):
        self.sock=sock
    def do_list(self):
        self.sock.send(b"LIST")
        result=self.sock.recv(128).decode()
        if result=='OK':
            file=self.sock.recv(1024*1024).decode()
            print(file)
        else:
            print("文件库为空")

    def store_file(self,file_name):
        print(file_name)
        try:
            f=open(file_name,'rb')
        except:
            print("文件不存在")
            return
        file_name=file_name.split('/')[-1]
        data='STOR '+file_name
        self.sock.send(data.encode())
        result=self.sock.recv(128).decode()
        if result=='OK':
            sleep(0.1)
            while True:
                data=f.read(1024)
                # print(data.decode())
                if not data:
                    sleep(0.1)
                    self.sock.send(b'##')
                    break
                self.sock.send(data)
        else:
            print("文件已存在")

    def do_get(self, file_name):
        msg="RETR "+file_name
        self.sock.send(msg.encode())
        result=self.sock.recv(128).decode()
        if result=='OK':
            # print("有了")
            f=open(file_name,'wb')
            while True:
                data=self.sock.recv(1024)
                if data==b'##':
                    print("结束")
                    break
                f.write(data)
            f.close()
        else:
            print("文件不存在")

    def do_exit(self):
        self.sock.send(b'EXIT')
        self.sock.close()
        sys.exit('退出')


def main():
    sock=socket()
    sock.connect(ADDR)
    ftp=FTP_Client(sock)
    while True:
        print("=============命令选项=============")
        print("***           list            ***")
        print("***         get file          ***")
        print("***         put file          ***")
        print("***            exit           ***")
        print("=================================")
        cmd=input("请输入命令:")
        if cmd=="list":
            ftp.do_list()
        elif cmd=="stor":
            file_name=input("请输入要传输的文件名:")
            ftp.store_file(file_name)
        elif cmd=="get":
            file_name=input("请输入想要下载的文件名:")
            ftp.do_get(file_name)
        elif cmd=='exit':
            ftp.do_exit()
if __name__ == '__main__':
    main()

