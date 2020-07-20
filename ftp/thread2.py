from threading import *
from time import sleep
def fun(sec,name):
    print("含有参数的线程")
    sleep(sec)
    print("%s 线程执行完毕"%name)
jobs=[]
for i in range(5):
    t=Thread(target=fun,args=(2,),kwargs={'name':"T%d"%i})
    jobs.append(t)
    t.start()
[x.join() for x in jobs]
