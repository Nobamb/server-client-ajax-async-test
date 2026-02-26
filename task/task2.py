# task를 활용해서 여러개의 비동기 함수 실행
import asyncio


# task에서 받은 값을 기반으로
# 함수를 실행하도록 함
async def task_after(task):
    # 대기 한 후 task값 받기
    result = await task

    print("task_after 시작")
    # 대기
    await asyncio.sleep(2)
    # 결과 출력
    print(f"결과: {result}")


# task에서 값 저장
async def task_result(value):

    # task_result 시작 알림
    print("task_result 시작")
    await asyncio.sleep(2)
    # value를 f-string으로 지정
    result = f"task_result 값 {value}"
    # result를 return
    return result



# main 실행
async def main():

    # task 지정
    task1 = asyncio.create_task(task_result(1))
    task2 = asyncio.create_task(task_result(2))

    # gather를 통해 여러개 지정
    await asyncio.gather(task_after(task1), task_after(task2))

    print("비동기 완료")


print("시작")
# 비동기 시작
asyncio.run(main())
print("마무리")
