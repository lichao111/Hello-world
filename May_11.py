#!user/bin/env python
import multiprocessing
import time

def func(msg):
    print "msg:", msg
    time.sleep(3)
    print "end"

if __name__ == "__main__":
    print "start_time:",time.ctime()
    pool = multiprocessing.Pool(processes = 5)
    for i in xrange(5):
        msg = "hello %d" %(i)
        pool.apply_async(func, (msg, ))   

    print "Mark~ Mark~ Mark~~~~~~~~~~~~~~~~~~~~~~"
    pool.close()
    pool.join()  
    print "Sub-process(es) done."
    print "end_time:",time.ctime()
def m1(x): 
    print x * x
    time.sleep(3) 

if __name__ == '__main__':
    print time.ctime() 
    pool = multiprocessing.Pool(multiprocessing.cpu_count()) 
    i_list = range(4)
    pool.map(m1, i_list)
    print time.ctime()
