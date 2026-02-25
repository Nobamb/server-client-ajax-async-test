// 1. 자바스크립트에서의 병렬 데이터 공유 (Future 방식)
// 자바스크립트에서도 Promise를 먼저 만들어 배포하고, 나중에 resolve를 호출해 대기하던 모든 함수를 동시에 깨울 수 있습니다.
// JavaScript
// 1. "미래의 값"을 담을 바구니(Promise)를 미리 만듭니다.
let resolveData;
const sharedPromise = new Promise((resolve) => {
    resolveData = resolve; // 나중에 값을 채울 스위치를 외부 변수에 저장
});

// 2. 여러 비동기 함수들이 이 하나의 Promise를 지켜보게 합니다 (await)
async function consumerA() {
    console.log("A: 데이터 대기 중...");
    const result = await sharedPromise; // 여기서 멈춤
    console.log("A: 공유 완료 ->", result);
}

async function consumerB() {
    console.log("B: 나도 대기 중...");
    const result = await sharedPromise; // 여기서 멈춤
    console.log("B: 공유 완료 ->", result);
}

// 3. 지연 시간 후 값을 딱 한 번만 넣어줍니다 (Python의 set_result)
async function producer() {
    console.log("프로듀서: 작업 중... (2초 소요)");
    await new Promise(r => setTimeout(r, 2000)); // sleep(2) 역할
    
    console.log("프로듀서: 데이터 확정!");
    resolveData("2026 대박 기운"); // 이 순간 A와 B가 동시에 깨어남!
}

consumerA();
consumerB();
producer();
