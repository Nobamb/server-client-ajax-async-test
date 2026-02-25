# future을 사용하는 상황

import asyncio

async def waiter(name, future):
    print(f"[{name}] 결과를 기다리는 중...")
    # 여기서 멈춥니다. 누군가 future.set_result()를 해줄 때까지!
    result = await future 
    print(f"[{name}] 드디어 결과 도착: {result}")

async def worker(future):
    print("[일꾼] 3초 뒤에 결과를 보내줄게...")
    await asyncio.sleep(3)
    # 여기서 값을 뙇! 하고 꽂아줍니다. 그러면 기다리던 waiter가 깨어납니다.
    future.set_result("황금 열쇠") 

async def main():
    loop = asyncio.get_running_loop()
    shared_future = loop.create_future()

    # 두 명은 기다리고, 한 명은 나중에 값을 채워줍니다.
    await asyncio.gather(
        waiter("A", shared_future),
        waiter("B", shared_future),
        worker(shared_future)
    )

asyncio.run(main())



# future이 의미 없는 상황


# # asyncio 가져오기
# import asyncio


# # future 사용해보기


# # 비동기 함수 try_future

# async def try_future(n):
#     # asyncio의 future 지정1
#     future = asyncio.Future()
#     # asyncio의 future 지정2
#     # loop = asyncio.get_event_loop()
#     # future = loop.create_future()
#     # future의 메소드 실행
#     # set_result()
#     future.set_result(n)
#     print(f"{n}번째 try_future")
#     await asyncio.sleep(1)
#     print(f"{n}번째 try_future 동작 이후1")
#     print(f"{n}번째 try_future 동작 이후2")
#     print(f"{n}번째 try_future 동작 이후3")
#     print(f"{n}번째 try_future 동작 이후4")
#     print(f"{n}번째 try_future 동작 이후5")



# # main 비동기 함수
# async def main():
    
#     max_index = 6
#     for i in range(max_index):
#         await try_future(i+1) 

    
#     print("main 비동기 동작 완료")


# asyncio.run(main())