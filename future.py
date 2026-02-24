# future로 비동기 작업해보자

# 자바스크립트로 Promise를 해보았을 때

# const promiseTest = (n) => {

# return new Promise((resolve, reject)=> {


# console.log(n)
# resolve를 통해서 값을 전달
# resolve(n+1)


# })


# }


# promiseTest(0).then((n)=>promiseTest)


# 파이썬 future로도 테스트

import asyncio


def promise_test(n):
    # 1. 새로운 Future 객체를 생성 (JS의 new Promise)
    loop = asyncio.get_event_loop()
    future = loop.create_future()

    # 초기값 지정
    num = 0

    for i in range(n):
        num += i

    print(num)
    # 2. resolve(n+1)과 동일한 역할
    # 이 메서드를 호출하는 순간, 이 Future를 기다리던 곳에 값이 전달됩니다.
    future.set_result(n + 1)

    return future


async def main():
    # 3. .then()과 유사한 await 체이닝
    n1 = await promise_test(40000000)
    n2 = await promise_test(n1)
    n3 = await promise_test(n2)
    n4 = await promise_test(n3)

    n5 = await promise_test(n4)
    n6 = await promise_test(n5)

    await promise_test(n6)


# 동작 시작 알림
print("동작 시작")
# 이벤트 루프 실행
asyncio.run(main())
print("동기 동작")
