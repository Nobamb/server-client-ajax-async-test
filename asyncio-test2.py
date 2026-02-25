# asyncio 가져옴
import asyncio


# # 만약에 비동기 함수 없이 ========================================================
# # asyncio 실행하였을 경우


# # hello
# C:\Users\V\Documents\개발\server-client-ajax-async-test\asyncio-test2.py:10: RuntimeWarning: coroutine 'sleep' was never awaited
#   asyncio.sleep(1)
# RuntimeWarning: Enable tracemalloc to get the object allocation traceback
# world
# Traceback (most recent call last):
#   File "C:\Users\V\Documents\개발\server-client-ajax-async-test\asyncio-test2.py", line 18, in <module>      
#     asyncio.run(no_async())
#     ~~~~~~~~~~~^^^^^^^^^^^^
#   File "C:\Python314\Lib\asyncio\runners.py", line 204, in run
#     return runner.run(main)
#            ~~~~~~~~~~^^^^^^
#   File "C:\Python314\Lib\asyncio\runners.py", line 103, in run
#     raise TypeError('An asyncio.Future, a coroutine or an '
#                     'awaitable is required')
# TypeError: An asyncio.Future, a coroutine or an awaitable is required


# def test():
#     print("hello")
#     asyncio.1sleep(1)
#     print("world")


# def no_async():
#     test()    
    
# # asyncio 실행
# asyncio.run(no_async())



# 비동기 함수 예시=========================================


async def test1():
    # 1
    print("hello1")
    await asyncio.sleep(1)
    # 2
    print("world1")

async def test2():
    # 2
    print("hello2")
    await asyncio.sleep(1)
    # 3
    print("world2")
    
async def test3():
    # 3
    print("hello3")
    await asyncio.sleep(1)
    # 4
    print("world3")
    
    
# 직렬 사용(asyncio.gather 사용 x) ================================================
# async def async_func():
#     await test1()
#     await test2()
#     await test3()
#     await asyncio.sleep(2)
#     # 5
#     print("완료")
    
    
    
    
    
    
    
    
    
    
    
# 병렬 사용(asyncio.gather 사용 o) ===================================================

# (시작)
# hello1
# hello2
# hello3
# (test1,2,3 실행 1초 뒤)
# world1
# world2
# world3
# (시작 2초 뒤)
# 완료
# 마무리

async def async_func():
    await asyncio.gather(test1(),test2(),test3())
    print("완료")
    
    
    
    
# # 비동기 함수를 asynccio.run 없이 실행하였을 경우 ==================================================
# # 그냥 실행
# RuntimeWarning: coroutine 'async_func' was never awaited
#   async_func()
# RuntimeWarning: Enable tracemalloc to get the object allocation traceback
# 마무리

# async_func()

# asyncio.run으로 실행 ===================================================
# (모범답안)

# hello1
# (1초 뒤)
# world1
# hello2
# (1초 뒤)
# world2
# hello3
# (1초 뒤)
# world3
# (2초 뒤)
# 완료
# 마무리

asyncio.run(async_func())

# 마무리(비동기 외부의 동작)
# 6
print("마무리")