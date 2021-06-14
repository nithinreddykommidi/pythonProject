'''
1. threading.activeCount(): Returns the number of total Python thread that are active. 

'''

import threading
import time


def fun1():
    time.sleep(2)

def fun2():
    print(' \n Total threads count is :::::', threading.activeCount())


t1 = threading.Thread(target=fun1)
t2 = threading.Thread(target=fun2)

t1.start()
t2.start()



