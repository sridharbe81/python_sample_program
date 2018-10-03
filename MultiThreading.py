#Normal Program for sqauring and Cube the list of numbers
import time

def square(list):
    sq_list= []
    for i in list:
        time.sleep(0.2)
        sq_list.append(i*i)
    print('Square of the numbers are:', sq_list)

def cube(list1):
    cu_list=[]
    for i in list1:
        time.sleep(0.2)
        cu_list.append(i*i*i)
    print('Cube of the numbers are:', cu_list)

t= time.time()
square([1,2,3,4])
cube([10,20,20])
print('Total time took for this program to run:', time.time()-t)

print('*' *1000)
#the above program with multithreading concepts

import time
import threading
import subprocess

def cube(list):
    #cu_list =[]
    for i in list:
        time.sleep(0.2)
         # cu_list.append(i*i*i)
    print('Cube of numbers are :', i*1)

def config():
    print("Listing the Directory")
    time.sleep(0.2)
    output=subprocess.check_output(['ipconfig'])
    print(output)

def arp():
    print("Listing the Arp Details")
    time.sleep(0.2)
    output1 =subprocess.check_output(['arp','-a'])
    print(output1)

def square(list):
    for i in list:
        time.sleep(0.2)
    print('Sqaure of numbers are:', i*i*i)

t= time.time()
list = (10,20,30,40)

t1=threading.Thread(target=cube,args=(list,))
t2=threading.Thread(target=square,args=(list,))
t3=threading.Thread(target=config)
t4=threading.Thread(target=arp)

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()
print('Total time took for this program to run:', time.time()-t)
