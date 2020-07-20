import threading
from time import sleep
a=1
def music():
    global a
    a = 20
    for i in range(3):
        sleep(2)
        print("播放:大花轿")

t=threading.Thread(target=music)
t.start()
for i in range(4):
    sleep(1)
    print("播放:葫芦娃")
print(a)
t.join()
