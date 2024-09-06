const start = document.querySelector(".start");
const qna = document.querySelector(".qna");
const food = document.querySelector(".food_info");
const flavor = document.querySelector(".flavor_info");
const taste = document.querySelector(".taste_info");
const profile = document.querySelector(".profile_info");
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
// function next1(){
//     food.style.display = "none";
//     flavor.style.display = "block";

//     window.scrollTo({
//         top: 0,
//         behavior: 'smooth'
//     });
// }

// food -> flavor : 답변 필수 선택하게 하는 코드
function next1(){
    const selectFood = document.querySelector('input[name="food"]:checked');

    if (!selectFood) {
        alert("답변을 선택해 주세요.");
    } else {
        food.style.display = "none";
        flavor.style.display = "block";
        
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    }
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
// function next2(){
//     flavor.style.display = "none";
//     taste.style.display = "block";

//     window.scrollTo({
//         top: 0,
//         behavior: 'smooth'
//     });
// }

// flavor -> taste : 답변 필수 선택하게 하는 코드
function next2(){
    const selectFlavor = document.querySelector('input[name="flavor"]:checked');

    if (!selectFlavor) {
        alert("답변을 선택해 주세요.")
    } else {
        flavor.style.display = "none";
        taste.style.display = "block";

        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    }
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

// taste -> profile
// function next3(){
//     taste.style.display = "none";
//     profile.style.display = "block";

//     window.scrollTo({
//         top: 0,
//         behavior: 'smooth'
//     });
// }

// taste -> profile : 답변 필수 선택하게 하는 코드
function next3(){
    const selectSweetness = document.querySelector('input[name="sweetness"]:checked');
    const selectAcidity = document.querySelector('input[name="acidity"]:checked');
    const selectTannin = document.querySelector('input[name="tannin"]:checked');
    const selectIntensity = document.querySelector('input[name="intensity"]:checked');
    const selectBody = document.querySelector('input[name="body"]:checked');

    if (!selectSweetness || !selectAcidity || !selectTannin || !selectIntensity || !selectBody) {
        alert("답변을 선택해 주세요")
    } else {
        taste.style.display = "none";
        profile.style.display = "block";

        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    }
}

// taste <- profile
function pre3(){
    profile.style.display = "none";
    taste.style.display = "block";

    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
}

// profile -> result
function end(){
    profile.style.display = "none";
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

