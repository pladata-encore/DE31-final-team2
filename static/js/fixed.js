// 사이드 메뉴 열기 버튼 클릭 시
document.querySelector('.sideMenu').addEventListener('click', function() {
    document.querySelector('.detail_user_menu').classList.toggle('active');
});

// 사이드 메뉴 닫기 버튼 클릭 시
document.querySelector('.sideClose').addEventListener('click', function() {
    document.querySelector('.detail_user_menu').classList.remove('active');
});