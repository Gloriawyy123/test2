import threading
import time
from queue import Queue
import copy


####定义一个函数，实现某个功能，以便把他放到后面的线程里
def job(l,q):
    res = sum(l)
    q.put(res)


####定义多线程
def multi(l):
    q = Queue()
    threads = []
    for i in range(4):
        t = threading.Thread(target=job,args=(copy.copy(l),q), name='T%i'% i)
        t.start()
        threads.append(t)
    [t.join() for t in threads]
    total = 0
    for _ in range(4):
        total += q.get()
    print(total)


######定义一个正常的函数
def normal(l):
    total = sum(l)
    print(total)


###主函数
if __name__ == '__main__':
    l = list(range(1000000))
    a = time.time()
    print(a)
    normal(l*4)
    # time.sleep(1)
    b = time.time()
    print('nomal:', b-a)
    print(b)
    c = time.time()
    print(c)
    multi(l)
    d = time.time()
    print('multi:', time.time()-c)
