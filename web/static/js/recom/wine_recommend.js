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

// food parent, child 분류해서 선택할 수 있게 하는 방법
document.addEventListener('DOMContentLoaded', function() {
    const food_child = document.querySelector(".food_child");

    const meatBtn = document.getElementById('meatBtn');
    const seafoodBtn = document.getElementById('seafoodBtn');
    const cheeseBtn = document.getElementById('cheeseBtn');
    const appeDessertBtn = document.getElementById('appeDessertBtn');
    const etcBtn = document.getElementById('etcBtn');

    const meat = document.getElementById('meat');
    const seafood = document.getElementById('seafood');
    const cheese = document.getElementById('cheese');
    const appeDessert = document.getElementById('appeDessert');
    const etc = document.getElementById('etc');

    meatBtn.addEventListener('click', function() {
        showFoodChild();
        hideAllCategories();
        // food_child.style.display = 'block';
        meat.style.display = 'block';
    });

    seafoodBtn.addEventListener('click', function() {
        showFoodChild();
        hideAllCategories();
        seafood.style.display = 'block';
    });

    cheeseBtn.addEventListener('click', function() {
        showFoodChild();
        hideAllCategories();
        cheese.style.display = 'block';
    });

    appeDessertBtn.addEventListener('click', function() {
        showFoodChild();
        hideAllCategories();
        appeDessert.style.display = 'block';
    });

    etcBtn.addEventListener('click', function() {
        showFoodChild();
        hideAllCategories();
        etc.style.display = 'block';
    });

    function showFoodChild() {
        food_child.style.display = 'block';
        food_child.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }

    function hideAllCategories() {
        meat.style.display = 'none';
        seafood.style.display = 'none';
        cheese.style.display = 'none';
        appeDessert.style.display = 'none';
        etc.style.display = 'none';
    }
});

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

// taste 자동 스크롤
document.addEventListener('DOMContentLoaded', function() {
    // sweetness -> acidity
    const sweetnessRadios = document.querySelectorAll('input[name="sweetness"]');
    sweetnessRadios.forEach(function(radio) {
        radio.addEventListener('change', function() {
            document.getElementById('acidity_box').scrollIntoView({ behavior: 'smooth', block: 'center' });
        });
    });

    // acidity -> tannin
    const acidityRadios = document.querySelectorAll('input[name="acidity"]');
    acidityRadios.forEach(function(radio) {
        radio.addEventListener('change', function() {
            document.getElementById('tannin_box').scrollIntoView({ behavior: 'smooth', block: 'center' });
        });
    });

    // tannin -> intensity
    const tanninRadio = document.querySelectorAll('input[name="tannin"]');
    tanninRadio.forEach(function(radio) {
        radio.addEventListener('change', function() {
            document.getElementById('intensity_box').scrollIntoView({ behavior: 'smooth', block: 'center' });
        });
    });

    // intensity -> body
    const intensityRadio = document.querySelectorAll('input[name="intensity"]');
    intensityRadio.forEach(function(radio) {
        radio.addEventListener('change', function() {
            document.getElementById('body_box').scrollIntoView({ behavior: 'smooth', block: 'center' });
        });
    });

});

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

// profile 자동 스크롤
document.addEventListener('DOMContentLoaded', function() {
    // alcohol_box의 radio 버튼이 선택되면 price_box로 스크롤
    const alcoholRadios = document.querySelectorAll('input[name="alcohol"]');
    alcoholRadios.forEach(function(radio) {
        radio.addEventListener('change', function() {
            document.getElementById('price_box').scrollIntoView({ behavior: 'smooth', block: 'center' });
        });
    });

    // price_box의 radio 버튼이 선택되면 type_box로 스크롤
    const priceRadios = document.querySelectorAll('input[name="price"]');
    priceRadios.forEach(function(radio) {
        radio.addEventListener('change', function() {
            document.getElementById('type_box').scrollIntoView({ behavior: 'smooth', block: 'center' });
        });
    });
});

// profile -> result
// function end(){
//     profile.style.display = "none";
//     result.style.display = "block";

//     window.scrollTo({
//         top: 0,
//         behavior: 'smooth'
//     });
// }

// profile -> result : 답변 필수 선택하게 하는 코드
function end(){
    const selectAlcohol = document.querySelector('input[name="alcohol"]:checked');
    const selectPrice = document.querySelector('input[name="price"]:checked');
    const selectType = document.querySelector('input[name="type"]:checked');

    if (!selectAlcohol || !selectPrice || !selectType) {
        alert("답변을 선택해 주세요")
    } else {
        profile.style.display = "none";
        result.style.display = "block";

        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    }
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
        
        // 페이지의 최하단으로 이동
        document.documentElement.scrollIntoView({ behavior: 'smooth', block: 'end' });

    } else { // 다른 체크박스 선택 시
        const noneCheckbox = document.querySelector('input[name="flavor"][value=""]');
        if (noneCheckbox) {
            noneCheckbox.checked = false; // "상관 없음" 체크 해제
        }
    }
}