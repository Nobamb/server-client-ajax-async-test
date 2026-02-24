import asyncio

# 1. 이제 이 함수는 진짜 비동기 함수입니다. (async def)
async def promise_test(n):
    print(f"{n} 작업 시작!")
    
    # for문 대신, 진짜 비동기로 1초간 대기 (이때 이벤트 루프가 다른 일을 하러 떠남!)
    await asyncio.sleep(1) 
    
    print(f"{n} 작업 완료!")
    return n + 1

async def main():
    # 2. 비동기의 꽃: 병렬 실행! (Promise.all 과 동일한 역할)
    # n1부터 n6까지 동시에 출발시킵니다.
    print("비동기 병렬 실행 시작!")
    results = await asyncio.gather(
        promise_test(1),
        promise_test(2),
        promise_test(3),
        promise_test(4),
        promise_test(5),
        promise_test(6),         
        promise_test(7),
        promise_test(8),
        promise_test(9),
        promise_test(10),
        promise_test(11),
        promise_test(12)
    )
    print("모든 비동기 완료:", results)

print("프로그램 시작")
asyncio.run(main()) # 여기서 다 끝날 때까지 대기
print("프로그램 완전히 종료 (동기 동작)")
