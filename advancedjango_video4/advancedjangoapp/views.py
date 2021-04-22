from django.shortcuts import render, HttpResponse
import time
import threading
from .models import Student
import asyncio

from asgiref.sync import sync_to_async, async_to_sync
from channels.db import database_sync_to_async
async def func3():
    return HttpResponse("Done")
def func2():
    return func3()
def func(): 
    return func2()

def index(request):
    print("index:" + str(threading.get_native_id()))
    a = func
    #a._is_coroutine = asyncio.coroutines._is_coroutine
    print(asyncio.iscoroutinefunction(a))

    return async_to_sync(a)()



async def help_func():
    # time.sleep(20)
    # await asyncio.sleep(20)
    #time.sleep(20)
    print("help_func:" + str(threading.get_native_id()))
    #students = Student.objects.all()
    #print(students)



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








