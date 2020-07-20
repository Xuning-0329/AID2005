from socket import *
from threading import Thread
import os
from time import sleep

FTP='../../day14/'
file_list=os.listdir(FTP)
# print(file_list)
HOST='0.0.0.0'
PORT=8889
ADDR=(HOST,PORT)
class FTP_Server(Thread):
    def __init__(self,connfd):
        super().__init__()
        self.connfd=connfd
    def run(self):
        while True:
            msg = self.connfd.recv(1024).decode()
            if not msg or msg=='EXIT':
                self.connfd.close()
                return
            else:
                tmp = msg.split(' ', 1)
                if tmp[0]=='LIST':
                    self.do_list()
                elif tmp[0] =='STOR':
                     self.store_file(tmp[1])
                elif tmp[0] == 'RETR':
                    self.do_get(tmp[1])

    def do_list(self):
        file_list = os.listdir(FTP)
        if not file_list:
            self.connfd.send(b'FAIL')
            return
        else:
            self.connfd.send(b'OK')
            sleep(0.1)
            data='\n'.join(file_list)
            self.connfd.send(data.encode())

    def store_file(self, file_name):
        if os.path.exists(FTP+file_name):
            self.connfd.send(b'FAIL')
            return
        else:
            self.connfd.send(b'OK')
            f=open(FTP+file_name,'wb')
            while True:
                data=self.connfd.recv(1024)
                if data==b'##':
                    print("结束")
                    break
                f.write(data)
            f.close()


    def do_get(self, file_name):
        try:
            f=open(FTP+file_name,'rb')
        except:
            self.connfd.send(b'FAIL')
        else:
            self.connfd.send(b'OK')
            sleep(0.1)
            while True:
                data=f.read(1024)
                # print(data.decode())
                if not data:
                    sleep(0.1)
                    self.connfd.send(b'##')
                    break
                self.connfd.send(data)
def main():
    sock=socket()
    sock.bind(ADDR)
    sock.listen(5)
    while True:
        connfd,addr=sock.accept()
        t=FTP_Server(connfd)
        t.start()

if __name__ == '__main__':
    main()
