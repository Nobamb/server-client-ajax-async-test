# task로 비동기 작업 해보기
import asyncio



# 임의의 비동기 지정
async def async_fn(name):
    # 비동기 동작 지정
    # 2초 지연
    await asyncio.sleep(2)

    # name 리턴
    return name





# 비동기 main 지정
async def main():
    
    # main 시작 알림
    print("main 시작")
    
    # task 지정
    task = asyncio.create_task(async_fn("홍길동"))
    
    # task를 받도록 기다리다가 저장
    result = await task
    
    # 출력
    print(result)



# asyncio.run 실행
print("시작")
asyncio.run(main())
print("마무리")