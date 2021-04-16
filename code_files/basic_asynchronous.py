import threading
from threading import Thread
import time
import multiprocessing
from multiprocessing import Process
import asyncio

async def async_help_func():
    loop = asyncio.get_running_loop()
    print(loop)
    for i in range(10):
        await asyncio.sleep(2)
        print(threading.active_count()) #actual user threads at this particular time
        print(str(threading.get_native_id()) + "first thread: "+ str(i))
    
async def mainfunc():
    loop = asyncio.get_running_loop()
    print(loop)
    start_time = time.time()
    #await asyncio.gather(loop.create_task(async_help_func()), loop.create_task(async_help_func()))
    await asyncio.gather(async_help_func(), async_help_func())

    # loop.create_task(async_help_func())
    # loop.create_task(async_help_func())

    # same as asyncio.create_task()
    # asyncio.ensure_future(async_help_func())

    


    end_time = time.time()
    result = end_time - start_time
    print(result)

# if __name__ == '__main__':
#     asyncio.run(mainfunc())

#mainfunc()


# for using the run_until_complete which work like "await loop.create_task()"
# You will have to create a new event loop in a thread which do not contains any eventloop
# if the eventloop exist already get_event_loop will return the running_loop
# as on one thread only one eventloop can be there

# loop = asyncio.get_event_loop()
# print(loop)
# try:
#     loop.run_until_complete(async_help_func())
# finally:
#     loop.stop()

import asyncio
import threading
class Middleware():
    def __init__(self):
        print("init method middleware " + str(threading.get_native_id()))
        #print(asyncio.get_running_loop())
        self._is_coroutine = asyncio.coroutines._is_coroutine

    def __call__(self):
        return self.__acall__()

    async def __acall__(self):
        print(threading.get_native_id())
        print(asyncio.get_running_loop())
        #self._is_coroutine = asyncio.coroutines._is_coroutine
        return 2
    
    async def test(self):
        print("This is test method of middleware")
        return 2

class TestAsync():   
    def __init__(self):
        print("init method TestAsync")
        print(threading.get_native_id())
        #print(asyncio.get_running_loop())


    async def __call__(self):
        print("call testasync thread: " + str(threading.get_native_id()))
        print(asyncio.get_running_loop())
        a = Middleware()
        print("is call method of middleware async? - " + str(asyncio.iscoroutinefunction(a)))
        print("is test method of middleware async? - " + str(asyncio.iscoroutinefunction(a.test)))
        b = await a()
        print(type(b))
        c = await a.test()
        print(type(c))


if __name__ == '__main__':
    a = TestAsync()
    asyncio.run(a())


