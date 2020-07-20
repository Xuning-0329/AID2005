from threading import Lock,Thread
lock01=Lock()
lock02=Lock()
def print_atoz():
    for i in range(65,91):
        lock02.acquire()
        print(chr(i),end='')
        lock01.release()
def print_num():
    for i in range(1, 53, 2):
        lock01.acquire()
        print("%d%d" % (i, i + 1), end='')
        lock02.release()
t1=Thread(target=print_num)
t2=Thread(target=print_atoz)
lock02.acquire()
t1.start()
t2.start()
t1.join()
t2.join()
