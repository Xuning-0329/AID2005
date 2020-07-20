from threading import *
from time import sleep
ticket_list=[]
for i in range(1,501):
    ticket_list.append("T%d"%i)

print(ticket_list)
def book_ticket(window):
    global ticket_list
    while True:
        sleep(0.1)
        if(len(ticket_list)==0):
            break
        ticket=ticket_list[0]
        del ticket_list[0]
        print(f"{window}---{ticket}")
jobs=[]
for i in range(1,11):
    window="w%d"%i
    t=Thread(target=book_ticket,args=(window,))
    t.start()
[x.join() for x in jobs]