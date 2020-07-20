from threading import Event,Thread
msg=None
e=Event()
def yzr():
    print("杨子荣前来拜山头")
    global msg
    msg="天王盖地虎"
    e.set()
t=Thread(target=yzr)
t.start()
print("说对口令才是自己人")
e.wait()
if msg=="天王盖地虎":
    print("宝塔镇河妖")
    print("欢迎")
else:
    print("打死他,,,,")
