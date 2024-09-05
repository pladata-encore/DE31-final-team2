const start = document.querySelector(".start");
const qna = document.querySelector(".qna");
const food = document.querySelector(".food_info");
const flavor = document.querySelector(".flavor_info");
const taste = document.querySelector(".taste_info");
const main = document.querySelector(".main_info");
const result = document.querySelector(".result");

// start -> food
function begin(){
    start.style.display = "none";
    food.style.display = "block";
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
}

// food -> flavor
function next1(){
    food.style.display = "none";
    flavor.style.display = "block";
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
}

// food <- flavor
function pre1(){
    flavor.style.display = "none";
    food.style.display = "block";
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
}

// flavor -> taste
function next2(){
    flavor.style.display = "none";
    taste.style.display = "block";
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
}

// flavor <- taste
function pre2(){
    taste.style.display = "none";
    flavor.style.display = "block";
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
}

// taste -> main
function next3(){
    taste.style.display = "none";
    main.style.display = "block";
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
}

// taste <- main
function pre3(){
    main.style.display = "none";
    taste.style.display = "block";
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
}

// main -> result
function end(){
    main.style.display = "none";
    result.style.display = "block";
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
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

