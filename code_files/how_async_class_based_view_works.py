import asyncio
from asgiref.sync import async_to_sync, sync_to_async
async def get():       
    return "Done"
def dispatch():
    return get()
def as_view():
    #dispatch()  # this will give error as not awaited if async function called directly without awaiting it
    return dispatch() # no error as when this as_view function is called it will return another async function 
    #return "hello"

@sync_to_async
def help():
    print("hello")
    return "hello"

def start():
    # async
    print(type(get))
    print(asyncio.iscoroutinefunction(get))
    print(type(get()))
    # sync_to_async
    print(type(help))
    print(asyncio.iscoroutinefunction(help))
    print(type(help()))
    #._is_coroutine
    a = as_view
    print(type(a))
    a._is_coroutine = asyncio.coroutines._is_coroutine
    print(type(a))
    print(type(a()))
    
    print(asyncio.iscoroutinefunction(a))
    if asyncio.iscoroutinefunction(a):
        result = async_to_sync(a)()   # async_to_sync or await demands a response of class 'coroutine' as a output
        print(result)
    else:
        result = a()
        print(result)

start()


# you can make a coroutine using 3 ways
# 1. async def func
# 2. @sync_to_async
#    def func()
# 3. 
# def func():
#     return "response"
# def func2():
#     a = func
#     a._is_coroutine = asyncio.coroutines._is_coroutine
#     result = a()   # this will work
#     result = async_to_sync(a)()   # not work





