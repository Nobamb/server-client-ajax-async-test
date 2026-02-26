// resolve 사용법

// Promise의 resolve는 정적 메소드라서
// 따로 생성자를 호출할 필요 없음
Promise.resolve("안녕").then(console.log)

// resolve를 미리 지정
const resolveResult = Promise.resolve("반가워")

// 지정한 후 then으로 console.log 실행
resolveResult.then((result)=>console.log(result))


// reject 사용법

// 기본은 new Error를 통해
// 임의의 에러를 출력함
// 에러를 출력하여 어디서 오류가 났는지 확인 가능

Promise.reject(new Error("문제 발생"))

// console.log를 통해
// 추가적으로 어느 부분에서 오류가 발생했는지 쉽게 확인 가능
Promise.reject(new Error("문제 발생2")).catch(err => console.log(`검출된 오류 ${err}`))