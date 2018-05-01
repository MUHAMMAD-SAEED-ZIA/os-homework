import time
from collections import OrderedDict
from operator import itemgetter
from array import *
tt=0

w_time=0
t_time=0
new_dic={}
count=0

def minimum():
    mini=next (iter (newk.keys()))
    for k in new_dic:
        if(new_dic[mini][2]>new_dic[k][2]):
            mini=k

    return mini;      

def wait_delete():
    for k in new_dic:
        start=0
        end=0
        it=0
        global tt
        #print(new_dic)
        if(new_dic[k][0]>tt):
            print "cpu idle for ",new_dic[k][0]-tt, " second"
            time.sleep(new_dic[k][0]-tt)
            tt+=new_dic[k][0]-tt
            it=new_dic[k][0]-tt
        start=tt
        time.sleep(new_dic[k][2])
        tt+=new_dic[k][2]
        end=tt

        print"\n",k, ":" ,new_dic[k]
        global w_time
        global t_time
        w_time+=start-int(new_dic[k][0])
        print"\n","waiting time= ",start-int(new_dic[k][0])

        #w_time.insert(k,start-int(new_dic[k][0]))
        print "\n"," turnaround ",end-int(new_dic[k][0])
        t_time+=end-int(new_dic[k][0])
        new_dic[k][2]=0
    print"\n","Average waiting time= ",w_time/count
    print"\n","Average turround time= ",t_time/count
    

       
def input():
    d={}
    j=0
    global count
    count=int(raw_input("how manty process you want to enter..?"))
    
    for j in range(count):
        a=float(raw_input("Enter arrival time"))
        d.setdefault(j, []).append(a)
        a=raw_input("Enter name")
        d.setdefault(j, []).append(a)
        a=float(raw_input("Enter burst time"))
        d.setdefault(j, []).append(a)
    print(d)
    global new_dic
    new_dic=OrderedDict(sorted(d.items(),key=itemgetter(1)))
    wait_delete()
#new_dic={1:[5,"sms",3],2:[7,"call",0],3:[9,"trap",0]}
input()

