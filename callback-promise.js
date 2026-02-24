// 콜백함수
// 비동기+작업를 구현해보려던 최초의 문법
// 콜백함수 자체만으로는 비동기x

// function increaseAndPrint(n, callback) {

// 동기 형태의 동작
//     const increased = n + 1;
//     console.log(increased);
//     if (callback) {
//       callback(increased); // 콜백함수 호출
//     }

// 비동기 형태의 동작
// 초창기부터 존재하던 setinterval은 비동기
//     setTimeout(() => {
//     const increased = n + 1;
//     console.log(increased);
//     if (callback) {
//       callback(increased); // 콜백함수 호출
//     }
//   }, 1000);
// }

// 콜백지옥의 문제 발생
// 가독성이 좋지 못함


// increaseAndPrint(0, n => {
//   increaseAndPrint(n, n => {
//     increaseAndPrint(n, n => {
//       increaseAndPrint(n, n => {
//         increaseAndPrint(n, n => {
//           console.log('끝!');
//         });
//       });
//     });
//   });
// });



// Promise
// 콜백함수의 콜백지옥을 개선하면서
// 비동기 작업을 하고자 나오게 됨
// Promise 내부 동작 자체만으로도 비동기 작업 가능

function increaseAndPrint(n) {
  return new Promise((resolve, reject) => {
    const increased = n + 1;
    console.log(increased);
    resolve(increased);

    // setTimeout(() => {
    //   const increased = n + 1;
    //   console.log(increased);
    //   resolve(increased);
    // }, 1000);
  });
}


// 가독성이 비교적 괜찮음
increaseAndPrint(0)
  .then((n) => {
    console.log(`현재값 ${n}`);
    return increaseAndPrint(n);
  })
  .then((n) => {
    console.log(`현재값 ${n}`);
    return increaseAndPrint(n);
  })
  .then((n) => {
    console.log(`현재값 ${n}`);
    return increaseAndPrint(n);
  })
  .then((n) => {
    console.log(`현재값 ${n}`);
    return increaseAndPrint(n);
  }); // 체이닝 기법


console.log("동기 작업")