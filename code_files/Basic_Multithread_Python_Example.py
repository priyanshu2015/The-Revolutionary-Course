import threading
from threading import Thread
import time
import multiprocessing
from multiprocessing import Process

def func1_thread1():
    for i in range(10):
        time.sleep(2)
        print(threading.active_count()) #actual user threads at this particular time
        print(str(threading.get_native_id()) + "first thread: "+ str(i))

def func2_thread2():
    for i in range(10):
        time.sleep(2)
        print(threading.active_count())
        print(str(threading.get_native_id()) + "second thread: "+ str(i))
    
import concurrent.futures
def mainfunc():
    start_time = time.time()
    # thread1 = Thread(target = func1_thread1)
    # thread2 = Thread(target = func2_thread2)
    # thread1.start()
    # thread2.start()
    # thread1.join()
    # thread2.join()

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(func1_thread1)
        executor.submit(func2_thread2)

    # func1_thread1()
    # func2_thread2()
    
    end_time = time.time()
    result = end_time - start_time
    print(result)

if __name__ == '__main__':
    mainfunc()


# proc1 = Process(target=func1_thread1)
#     proc1.start()
#     proc2 = Process(target=func2_thread2)
#     proc2.start()
#     proc1.join()
#     proc2.join()


import multiprocessing
from multiprocessing import Process
def print_func(continent='Asia'):
    print('The name of continent is : ', continent)
def multiprocessfunc():
    print("Number of cpu : ", multiprocessing.cpu_count())
    names = ['1','2']
    procs = []
    proc = Process(target=print_func)  # instantiating without any argument
    procs.append(proc)
    proc.start()

    # instantiating process with arguments
    for name in names:
        # print(name)
        proc = Process(target=print_func, args=(name,))
        procs.append(proc)
        proc.start()

    # complete the processes
    for proc in procs:
        proc.join()

    print("done")

# if __name__ == '__main__':
#     multiprocessfunc()

