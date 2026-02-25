// form 받아오기
const form = document.querySelector("form");

// form에 있는 버튼 가져오기
const button = form.querySelector("button");

// 결과를 보여줄 요소
const resultBox = document.getElementById("result-box");

// 이미지를 생성하는 함수

const imgMake = (src) => {
  // 이미지 요소를 생성
  const img = document.createElement("img");

  // 이미지를 result-box에 넣기

  resultBox.append(img);
  // imgBox의 이미지의 src를 파라미터 src로 지정
  img.src = src;
  // alt는 임의 지정
  resultBox.querySelector("img").alt = "지정 완료";
};

// 이름을 박아넣는 함수

const nameMake = (nameValue) => {
  // 이름을 지정
  const name = document.createElement("span");

  // 이미지를 result-box에 넣기

  resultBox.append(name);
  // imgBox의 이미지의 src를 파라미터 src로 지정
  name.innerText = nameValue;
};

const fetchFunc1 = (selectValue) => {
  // fetch 작업 진행
  // GET 요청
  // content-type application/json
  fetch(`https://pokeapi.co/api/v2/pokemon/${selectValue}/`)
    .then((res) => res.json())
    .then((data) => {
      // 받아온 데이터에서 이미지 주소 가져오기
      const imgData = data.sprites.front_default;
      console.log(data);
      console.log(imgData);
      //   imgMake에 이미지주소 대입
      imgMake(imgData);
    });
};

const fetchFunc2 = (selectValue) => {
  // fetch 작업 진행
  // GET 요청
  // content-type application/json
  fetch(`https://pokeapi.co/api/v2/pokemon-species/${selectValue}/`)
    .then((res) => res.json())
    .then((data) => {
      // 받아온 데이터에서 한국어 이름 가져오기
      const koreaName = data.names[2].name;
      //nameMake에 이름 대입
      nameMake(koreaName);
    });
};

// 버튼 누르면 console 찍힘
button.addEventListener("click", (e) => {
  // 이벤트 막기
  e.preventDefault();
  // console.log("연결 성공")

  // select의 값 가져옴
  const selectValue = document.querySelector("form").children[0].value;

  Promise.all([fetchFunc1(selectValue), fetchFunc2(selectValue)]);

  //   fetchFunc1(selectValue);
  //   fetchFunc2(selectValue);
});
