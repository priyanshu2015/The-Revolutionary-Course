from django.shortcuts import render, HttpResponse
import time
import threading
from .models import Student
import asyncio
# from channels.layers import get_channel_layer
from asgiref.sync import sync_to_async
async def func3():   #get
    return HttpResponse("Done")
def func2():  #dispatch
    return func3()
def func():   #as_view
    return func2()

def index(request):  #view
    print("index:" + str(threading.get_native_id()))
    # channel_layer = get_channel_layer()
    # await channel_layer.group_send("chat_first", {
    #                 'type': 'chat_message',
    #                 'message': "notification",
    #                 })
    a = func
    #a._is_coroutine = asyncio.coroutines._is_coroutine
    print(asyncio.iscoroutinefunction(a))

    return async_to_sync(a)()



async def help_func():
    # time.sleep(20)
    # await asyncio.sleep(20)
    #time.sleep(20)
    print("help_func:" + str(threading.get_native_id()))
    # students = Student.objects.all()
    #print(students)

from asgiref.sync import sync_to_async, async_to_sync
from channels.db import database_sync_to_async

@sync_to_async(thread_sensitive=False)
def help_func2():
    print("help 2:" + str(threading.get_native_id()))
    students = Student.objects.all()
    time.sleep(20)
    return students

#@sync_to_async(thread_sensitive=False)
async def home(request):
    print("home:" + str(threading.get_native_id()))
    #await asyncio.sleep(20)
    #time.sleep(20)
    #await asyncio.gather(help_func(), help_func())
    # thread1 = threading.Thread(target=help_func)
    # thread2 = threading.Thread(target=help_func)
    # thread1.start()
    # thread2.start()
    # thread1.join()
    # thread2.join()
    
    #time.sleep(20)   #i/o operation
    # for i in range(10000):
    #     print(i)
    #await sync_to_async(help_func)()
    #async_to_sync(help_func)()--
    
    #students = await help_func2()

    #students = Student.objects.all()
    #print(students)
    #time.sleep(10)

    #await help_func2()
    return HttpResponse("Home")



import requests
import aiohttp

@sync_to_async(thread_sensitive=False)
def callApi(request):
    print("callApi:" + str(threading.get_native_id()))
    result = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=1000&page=1&sparkline=false')
    time.sleep(10)
    #result = result.json()
    # students = Student.objects.all()
    # print(students)
    #print(result)

    # url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=1000&page=1&sparkline=false'
    # async with aiohttp.ClientSession() as session:
    #     async with session.get(url) as response:
    #         print("Status:", response.status)
    #         print("Content-type:", response.headers['content-type'])
    #         html = await response.json()
    return HttpResponse("Done")



# Converting CBV to async
from django.views.generic import ListView
from django.utils.decorators import classonlymethod
class ListStudents(ListView):
    template_name = "advancedjangoapp/list.html"  
    model = Student
    context_object_name = "students"

    @classonlymethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        view._is_coroutine = asyncio.coroutines._is_coroutine
        return view
    

    @sync_to_async
    def get_data(self):
        print("data:" + str(threading.get_native_id()))
        students = Student.objects.all()
        return list(students)
    
    @sync_to_async
    def help():
        return "hello"

    
    async def get(self, request, *args, **kwargs):
        print("get:" + str(threading.get_native_id()))
        print(type(self.get_data))
        if(asyncio.iscoroutinefunction(self.get_data)):
            print("true")
        else:
            print("false")
        students = await self.get_data()
        print("hello")
        return render(request, "advancedjangoapp/list.html", {'students':students})#await sync_to_async(Student.objects.all)()})





#@sync_to_async(thread_sensitive=False)
async def help_func3():
    print(" help thread:" + str(threading.get_native_id()))
    # time.sleep(10)
    # students = Student.objects.all()
    # print(students)
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=1000&page=1&sparkline=false'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])
            html = await response.json()
    # return list(students)

async def runafterresponse(request):
    print("thread:" + str(threading.get_native_id()))
    loop = asyncio.get_running_loop()
    loop.create_task(help_func3())
    return HttpResponse("Done")


def helper_func():
    a = 0
    for i in range(10000):
        print(i)
        a+=i
    #time.sleep(20)
    return a


async def case1_func(request):
    loop = asyncio.get_running_loop()
    start_time = time.time()
    a = helper_func()
    end_time = time.time()
    result = start_time - end_time
    print(loop)
    print(threading.get_native_id())
    return HttpResponse(str(a) + " Time Taken:" + str(result))

import queue as Queue
que = Queue.Queue()
def helper_func2():
    print("start")
    a = 0
    for i in range(1000):
        print(i)
        a+=i
    que.put(a)
    print("end")

import threading
def case2_func(request):
    loop = asyncio.get_running_loop()
    print(loop)
    start_time = time.time()
    thread1 = threading.Thread(target = helper_func2)
    thread1.start()
    thread1.join()
    a = 0
    while not que.empty():
        a = que.get()
    end_time = time.time()
    result = start_time - end_time
    return HttpResponse(str(a) + " Time Taken:" + str(result))

import requests
def helper_func3():
    print("start getting")
    url1 = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=1000&page=1&sparkline=false'
    data1 = requests.get(url1).json()
    url2 = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=1000&page=1&sparkline=false'
    data2 = requests.get(url2).json()
    time.sleep(5)
    print("finished")


def case2_func_part2(request):
    start_time = time.time()
    thread1 = threading.Thread(target = helper_func3)
    thread1.start()
    thread1.join()
    end_time = time.time()
    result = start_time - end_time
    return HttpResponse(" Time Taken:" + str(result))


def case3_func(request):
    loop = asyncio.get_running_loop()
    print(loop)
    start_time = time.time()
    print("start")
    students = Student.objects.all()
    time.sleep(5)
    print(students)
    print("end")
    end_time = time.time()
    result = end_time - start_time
    return HttpResponse(" Time Taken:" + str(result))

from asgiref.sync import sync_to_async
#@sync_to_async
def helper_func4():
    print("start")
    print(threading.get_native_id())
    time.sleep(5)
    students = Student.objects.all()
    time.sleep(10)
    print("ok")
    print(students)
    
    print("end")
    print(threading.get_native_id())
    return students

async def case4_func(request):
    loop = asyncio.get_running_loop()
    print(loop)
    start_time = time.time()
    print(threading.get_native_id())
    #students = await sync_to_async(helper_func4, thread_sensitive=True)()
    loop.create_task(sync_to_async(helper_func4, thread_sensitive=False)())
    #print(type(students))
    end_time = time.time()
    result = end_time - start_time
    return HttpResponse(" Time Taken:" + str(result))

import aiohttp
async def case6_func(request):
    loop = asyncio.get_running_loop()
    print(loop)
    start_time = time.time()
    print("start")
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=1000&page=1&sparkline=false'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])
            html = await response.json()
    #await asyncio.sleep(10)
    end_time = time.time()
    print("end")
    result = end_time - start_time
    return HttpResponse(" Time Taken:" + str(result))


async def case7_func(request):
    loop = asyncio.get_running_loop()
    print(loop)
    start_time = time.time()
    print(threading.get_native_id())
    print("start")
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=1000&page=1&sparkline=false'
    data1 = requests.get(url).json()
    end_time = time.time()
    result = end_time - start_time
    print("end")
    return HttpResponse(" Time Taken:" + str(result))


async def helper_func5(url):
    print("start")
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])
            html = await response.json()
    print("end")
    #print(html)

async def case9_func(request):
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=1000&page=1&sparkline=false'
    await asyncio.gather(helper_func5(url), helper_func5(url))

    # example of async stack not usable when using wsgi server
    loop = asyncio.get_running_loop()
    loop.create_task(helper_func5(url))
    return HttpResponse("Done")

@sync_to_async
def helper_func6():
    print("start")
    students = Student.objects.all()
    print(students)
    time.sleep(5)
    print("end")

#@sync_to_async
def helper_func7():
    print("start2")
    students = Student.objects.all()
    print(students)
    time.sleep(5)
    print("end2")

async def case10_func(request):
    await asyncio.gather(sync_to_async(helper_func6, thread_sensitive=False)(), sync_to_async(helper_func7, thread_sensitive=False)())
    return HttpResponse("Done")


from django.db import transaction
from .models import Account
@transaction.atomic
def database_race(request):
    a = Account.objects.first()
    if(a.amount>=1000):
        a.amount = a.amount - 1000
        print("amount deducted")
    else:
        print("no such amount")
    time.sleep(5)
    a.save()
    return HttpResponse("done")



from django.middleware import security

from django.middleware.clickjacking import XFrameOptionsMiddleware





