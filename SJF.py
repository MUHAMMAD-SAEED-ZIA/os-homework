import time
from collections import OrderedDict
from operator import itemgetter
from array import *
tt=0
flag=0        #flag for chk to idle time
w_time=0      #waiting time
t_time=0      #total time
newk={}       #input dictionary
new_dic={}    #ready dict
count=0       #number of input
#find minimum of new_dic
def minimum(mini):
  
    for k in new_dic:
        if(new_dic[k][2]!=0):

            if(new_dic[mini][2]>new_dic[k][2]):
                mini=k

    return mini;      

def minimum_dic(mini):
  
    for k in newk:
        if(newk[k][2]!=0):

            if(newk[mini][0]>newk[k][0]):
                mini=k

    return mini;

#main executation     
def wait_delete(k):
    if(new_dic[k][2]!=0):
        global flag
        flag=0
        start=0
        end=0
        global tt       
        start=tt
        time.sleep(new_dic[k][2])
        tt+=new_dic[k][2]
        end=tt

        print"\n",k, ":" ,new_dic[k]
        global w_time
        global t_time
        w_time+=start-int(new_dic[k][0])
        print "\n waiting = ",start-int(new_dic[k][0]),"total=  ", tt," turnaround=  ",end-int(new_dic[k][0])

        t_time+=end-int(new_dic[k][0])
        
        new_dic[k][2]=0
        newk[k][2]=0
         
       
def input():
    # j is key for dict
    j=0
    global count
    count=int(raw_input("how manty value you want to enter..?"))
    
    for j in range(count):
        a=float(raw_input("Enter arrival time"))
        newk.setdefault(j, []).append(a)
        a=raw_input("Enter name")
        newk.setdefault(j, []).append(a)
        a=float(raw_input("Enter burst time"))
        newk.setdefault(j, []).append(a)
    print(newk)
    #sort dict with first atribute
    #newk=OrderedDict(sorted(dic.items(),key=itemgetter(1)))
#newk={2:[5,"sms",5],3:[2,"call",5],1:[14,"trap",9],4:[8,"signal",2]}
input()

k=1
f=1
# chk to ensure burst time of all process is zero
while (f==1):
    for g in newk:
        if(newk[k][2]!=0):
            f=1
        else:f=0

    if(f==0):
        break
    for n in newk: 
        for m in newk :
            if(newk[m][0]<=tt and newk[m][2]!=0):
                t=m
                flag=1
                new_dic.setdefault(m, []).append(int(newk[m][0]))
                new_dic.setdefault(m, []).append(newk[m][1])
                new_dic.setdefault(m, []).append(newk[m][2])
                #sort dic with any atrebute
         #new_dic=sorted(newk.items(), key=lambda newk: newk[1][2])
        if(flag!=1):
            nm=minimum_dic(n)
            if(newk[nm][2]!=0):
                print "cpu idle for ",newk[nm][0]-tt, " second"
                time.sleep(newk[nm][0]-tt)
                tt+=newk[nm][0]-tt
                flag=0
               
        
        for ke in new_dic:
            if(new_dic[ke][2]!=0):
                 mn=minimum(t)
                 wait_delete(mn)
print("\n ","Average waiting time=  ",w_time/count)
print("\n"," Average total time=  ",t_time/count)
  