console.log("안녕")


// 1000초 후 작동
const await = 1000


// settimeout을 만나면 비동기로 이해하고
// 밑의 console.log("자니?"로 적용)
setTimeout(() => {
    console.log("하이")
}, await);


// 추가 console.log
console.log("자니")