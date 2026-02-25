# asyncio 가져옴
import asyncio


# add_done_callback 사용해보기
# add_done_callback은 then에 해당


# 비동기 작업 후 함수
async def async_after(value):
    # value 실행
    print("마무리 전")
    await asyncio.sleep(1)
    print(f"마무리 {value}")


# 비동기의 값 추가
# 비동기 강조하기 위해 sleep 2초 후 지정

async def async_set_value(value, future):


    # sleep 2초 지정
    await asyncio.sleep(2)
    # future에서 값 지정
    future.set_result(value)
    


# 임의의 비동기 함수
# async_set_value에서 지정한 값에다가
# value의 값을 더하도록 함
async def async_func(value, future):
    # future값 받아와서 지정
    before_result = await future
    # before_result에 value 더함
    result = before_result + value

    # 값 지정 후 
    # async_after 지정
    await async_after(result)



# 비동기 동작 실행
async def main():
    # asyncio에서 future 가져오기
    # future = asyncio.Future()
    future = asyncio.Future()
    
    # 비동기 함수에 값 대입
    await asyncio.gather(
        async_func(10, future), async_func(11, future), async_set_value(5, future)
    )
    print("완료")


print("시작")
# asyncio.run실행
asyncio.run(main())
print("끝")
