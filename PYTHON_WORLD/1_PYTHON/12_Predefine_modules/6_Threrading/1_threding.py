'''
1. Threading is used to run multiple jobs concurrently(at the same time)
2. Using threading module we can achive threading in python.
   target: the function to be executed by thread
   args  : the arguments to be passed to the target function
   name  : We can specify a name to the thread
   join  : Using join function we keep a thread to wait till ending the thread
'''
import threading
import time


def first_fun():
    print(' \n first_thread started')
    time.sleep(5)
    print(' \n first_thread ended')

def second_fun(a, b):
    print(' \n second_thread started')
    time.sleep(5)
    print(' \n second_thread ended')

#print(time.ctime())
#first_fun()
#second_fun(3,4)
#print(time.ctime())

ft = threading.Thread(target=first_fun)
st = threading.Thread(target=second_fun, args=('sriram','chowdary'))

print(' \n BEFIRE START ', time.ctime())
ft.start()
st.start()
st.join()
print(' \n AFTER END ' , time.ctime())


