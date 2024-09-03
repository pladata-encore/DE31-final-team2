const start = document.querySelector(".start");
const qna = document.querySelector(".qna");
const main = document.querySelector(".main_info");
const food = document.querySelector(".food_info");
const flavor = document.querySelector(".flavor_info");
const taste = document.querySelector(".taste_info");
const result = document.querySelector(".result");
// start -> qna
function begin(){
    start.style.display = "none";
    main.style.display = "block";
}

// qna 내에서 main_info -> flavor_info
function next1(){
    main.style.display = "none";
    food.style.display = "block";
}

// qna 내에서 flavor_info -> taste_info
function next2(){
    food.style.display = "none";
    flavor.style.display = "block";
    
}

// qna 내에서 flavor_info -> taste_info
function next3(){
    flavor.style.display = "none";
    taste.style.display = "block";
    
}

// qna 에서 result 로 이동
function next4(){
    taste.style.display = "none";
    result.style.display = "block";
}

// .flavor_info 관련 js
function handleCheckboxChange(checkbox) {
    const checkboxes = document.querySelectorAll('input[name="flavor"]');

    if (checkbox.value === "") { // "상관 없음" 선택 시
        checkboxes.forEach((cb) => {
            if (cb !== checkbox) {
                cb.checked = false; // 다른 체크박스 해제
            }
        });
    } else { // 다른 체크박스 선택 시
        const noneCheckbox = document.querySelector('input[name="flavor"][value=""]');
        if (noneCheckbox) {
            noneCheckbox.checked = false; // "상관 없음" 체크 해제
        }
    }
}
