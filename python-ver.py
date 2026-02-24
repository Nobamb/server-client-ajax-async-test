import asyncio

# 임의로 밀리 세컨드 값 불러옴
wait = 1000
# 밀리세컨드 값을 세컨드로 변환
wait_secont = wait / 1000

# 비동기 기반의 함수
async def main():
    print("안녕")
    await asyncio.sleep(wait_secont)
    print("반가워")
    

    
print("자니?")
asyncio.run(main())