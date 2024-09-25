# Wineasy 와인 추천 시스템
> 역할 및 팀원 소개
>
  > * 데이터 전처리 & 모델링 : 김소현, 김현지
  > 
  > * 프론트엔드 : 변수현
  > 
  > * 백엔드 : 신소영
  > 
  > * 환경 구축 : 조혜민 

## 1. 주제 선정 배경
### 와인을 보다 쉽게 즐길 수 있게 추천 시스템을 제작하고자 함
 
> gs25의 와인25플러스 서비스의 확산으로 와인에 대한 접근성은 낮아졌으나, 다른 주류에 비해 판매량은 적은 편이었다.
> 
> 소비자들이 와인에 대해 쉽게 접근할 수 있는 서비스가 있다면, 수요가 늘을 것이라 생각하여 '와인이지'를 제작하고자 함.
## 2. 서비스 개발을 위한 분석(NABC)
![image](https://github.com/user-attachments/assets/68fc2b61-abbb-45d8-af2c-4d22f006f2c6)


> * **아키텍처**
![image](https://github.com/user-attachments/assets/344bb1f9-98ee-41e8-85c9-f3dc00720ce3)

> Docker 환경 구성
jupyter notebook 과 mysql 을 컨테이너 환경에서 통합적으로 사용하기 위해 Docker 를 사용함.
AWS EC2 한 대에 아래와 같이 Docker 환경을 구성하여 데이터 수집 단계에서 활용함.
![image](https://github.com/user-attachments/assets/015908d0-f235-4f16-985a-72dd4c4418b4)


## 3. 데이터 전처리
* vivino 사이트에서 크롤링을 시도하였으나 ip가 차단되는 상황이 다수 발생
* 작업 시간을 줄이고자 ThreadPoolExecutor를 사용
* 정규표현식을 사용하여 와인 데이터를 가져옴
* Json 데이터를 변환하여 저장하였으나 None 오류가 다수 발생. 예외 처리를 하여 해결
* 예시 코드
```
  try:
    if style['body']:
      body = style['body']
  except:
    body = None
  ```
* EC2 환경 도커에 구축한 DB 적재 중 자료 소실
> docker-compose down으로 발생한 이슈로 확인.
>
> 다행히 백업DB가 있어서 다시 만들지는 않음.
>
> 백업을 생활화합시다.
* 유사도
> 초기 코사인 유사도 사용하였으나 원핫인코딩 데이터를 주로 사용하게 되어 유클리디안 유사도 적용

### 1. 데이터 확인

- 와인별 기본 통계
   
| 와인종류 | CNT | 최저가 | 최고가 | 평균 가격 | 최저 도수 | 최고 도수 | 평균 리뷰 갯수 | 평균 리뷰 점수 | 최저 바디감 | 최고 바디감 | 평균 바디감 | 최저 산도 | 최고 산도 | 평균 산도 | 최저 강도 | 최고 강도 | 평균 강도 | 최저 당도 | 최고 당도 | 평균 당도 | 최저 탄닌 | 최고 탄닌 | 평균 탄닌 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 레드와인 | 13,373 | 15 | 216,623,114 | 125,120 | 3.5 | 19.5 | 2,836 | 3.88 | 2 | 7.0171881349 | 4.05 | 1.4655045 | 5.4377997235 | 3.33 | 0.9677919791 | 5 | 3.84 | 0.4792504938 | 3.6649811 | 1.74 | 0.3669602234 | 4.7981215 | 3.02 |
| 화이트와인 | 4,219 | 15 | 135,338,644 | 70,856 | 6 | 16.5 | 1,729 | 3.83 | 1 | 5.6194959301 | 3.16 | 1.2889473 | 7.0610285106 | 3.66 | 0.1193825155 | 5 | 3.15 | 0.3227372117 | 3.5634208 | 1.79 | 0.6390123205 | 7.0299777632 | 2.77 |
| 스파클링와인 | 992 | 4,571 | 1,901,809 | 59,072 | 4.9 | 15 | 2,073 | 3.87 | 0.8472892833 | 4.1962783986 | 2.44 | 2.1072557345 | 6.8966850247 | 3.95 | 0.4955102395 | 4.9026639472 | 3.4 | 0.4179316114 | 4.6860800173 | 2.22 | 1.0745522661 | 6.1407849865 | 3.01 |
| 로제와인 | 340 | 6,154 | 1,479,293,224 | 4,373,407 | 9 | 15.3 | 1,845 | 3.77 | 2.8128723908 | 7.3496626563 | 4.48 | 1.6040479433 | 5.7982879923 | 3.05 | 1.106991825 | 4.9334938595 | 3.14 | 0.4906261309 | 2.2864104342 | 1.43 | 0.8229647745 | 3.8110323349 | 2.53 |
| 주정강화와인 | 213 | 11,627 | 226,390,754 | 1,126,419 | 11.5 | 21.5 | 1,654 | 3.99 | 2.5809254649 | 5.7419459566 | 4.77 | 1.3990419208 | 7.0635976673 | 3.18 | 3.134301 | 6.0229542451 | 4.71 | 1.7825328 | 5.033458329 | 3.89 | 1.3197546211 | 4.7049554885 | 3.1 |
| 디저트와인 | 235 | 4,926 | 919,061 | 66,226 | 2.3 | 20 | 1,329 | 4.08 | 1.0375555516 | 5 | 3.37 | 2.1019331878 | 7.4450627404 | 4.27 | 0.0758270924 | 5 | 3.34 | 1.4291449611 | 5 | 2.87 | 1.5805303883 | 4.447619 | 2.87 |

- 도수 분포

| 알콜 도수 범위 |	CNT |
| --- | --- |
| 12.5도 미만 |	1,882 |
| 12.5도 이상 14도 미만 |	8,991 |
| 14도 이상 16도 미만 |	8,164 |
| 16도 이상 |	335 |

- 와인 타입별 도수 분포
> 16도 이상에 해당하는 와인이 없는 종류가 있음

| type_id |	alcohol_range |	cnt |
| --- | --- | --- | 
| 레드 |	12.5도 미만	| 265 |
| 레드 |	12.5도 이상 14도 미만 |	5,553 |
| 레드 |	14도 이상 16도 미만	| 7,429 |
| 레드 |	16도 이상	| 126 |
| 화이트 |	12.5도 미만	| 728 |
| 화이트 |	12.5도 이상 14도 미만 |	2,850 |
| 화이트 |	14도 이상 16도 미만	| 637 |
| 화이트 |	16도 이상	| 4 |
| 스파클링 |	12.5도 미만	| 710 |
| 스파클링 |	12.5도 이상 14도 미만 |	270 |
| 스파클링 |	14도 이상 16도 미만	| 12 |
| 로제 |	12.5도 미만	| 70 |
| 로제 |	12.5도 이상 14도 미만 |	249 |
| 로제 |	14도 이상 16도 미만	| 21 |
| 디저트 |	12.5도 미만	| 107 |
| 디저트 |	12.5도 이상 14도 미만 |	67 |
| 디저트 |	14도 이상 16도 미만	| 38 |
| 디저트 |	16도 이상	| 23 |
| 주정강화 |	12.5도 미만	| 2 |
| 주정강화 |	12.5도 이상 14도 미만 |	2 |
| 주정강화 |	14도 이상 16도 미만	| 27 |
| 주정강화 |	16도 이상	| 182 |

- 가격대 분포 


| 가격 범위 |	CNT |
| --- | --- |
|1.5만원 미만 |	2,746 |
|1.5만원 이상 2.5만원 미만 |	4,961 |
|2.5만원 이상 3.5만원 미만 |	3,449 |
|3.5만원 이상 6만원 미만 |	4,080 |
|6만원 이상	| 4,136 |


- 와인 타입별 가격대 분포
> 주정강화는 1.5만원 미만이 거의 없고 로제 와인은 6만원 이상이 별로 없음 

- ~1.5만
  
| type_id	| price_range |	COUNT(*) |
| --- | --- | --- |
| 레드 |	1.5만 미만	| 1,769 |
| 레드 |	1.5만 이상 2.5만 미만	| 3,140 |
| 레드 |	2.5만 이상 3.5만 미만	| 2,312 |
| 레드 |	3.5만 이상 6만 미만	| 2,911 |
| 레드 |	6만 이상	| 3,241 |
| 화이트 |	1.5만 미만	| 697 |
| 화이트 |	1.5만 이상 2.5만 미만	| 1,334 |
| 화이트 |	2.5만 이상 3.5만 미만	| 864 |
| 화이트 |	3.5만 이상 6만 미만	| 801 |
| 화이트 |	6만 이상	| 523 |
| 스파클링 |	1.5만 미만	| 141 |
| 스파클링 |	1.5만 이상 2.5만 미만	| 253 |
| 스파클링 |	2.5만 이상 3.5만 미만	| 132 |
| 스파클링 |	3.5만 이상 6만 미만	| 217 |
| 스파클링 |	6만 이상	| 249 |
| 로제 |	1.5만 미만	| 104 |
| 로제 |	1.5만 이상 2.5만 미만	| 142 |
| 로제 |	2.5만 이상 3.5만 미만	| 57 |
| 로제 |	3.5만 이상 6만 미만	| 26 |
| 로제 |	6만 이상	| 11 |
| 디저트 |	1.5만 미만	| 23 |
| 디저트 |	1.5만 이상 2.5만 미만	| 44 |
| 디저트 |	2.5만 이상 3.5만 미만	| 45 |
| 디저트 |	3.5만 이상 6만 미만	| 66 |
| 디저트 |	6만 이상	| 57 |
| 주정강화 |	1.5만 미만	| 12 |
| 주정강화 |	1.5만 이상 2.5만 미만	| 48 |
| 주정강화 |	2.5만 이상 3.5만 미만	| 39 |
| 주정강화 |	3.5만 이상 6만 미만	| 59 |
| 주정강화 |	6만 이상	| 55 |

- ~2.5만
  
| type_id	| price_range |	COUNT(*) | 
| --- | --- | --- |
| 레드 | 2.5만 미만 | 4,909 |
| 레드 | 2.5만 이상 5만 미만 | 4,339 |
| 레드 | 5만 이상 | 4,125 |
| 화이트 | 2.5만 미만 | 2,031 |
| 화이트 | 2.5만 이상 5만 미만 | 1,445 |
| 화이트 | 5만 이상 | 743 |
| 스파클링 | 2.5만 미만 | 394 |
| 스파클링 | 2.5만 이상 5만 미만 | 270 |
| 스파클링 | 5만 이상 | 328 |
| 로제 | 2.5만 미만 | 246 |
| 로제 | 2.5만 이상 5만 미만 | 80 |
| 로제 | 5만 이상 | 14 |
| 디저트 | 2.5만 미만 | 67 |
| 디저트 | 2.5만 이상 5만 미만 | 89 |
| 디저트 | 5만 이상 | 79 |
| 주정강화 | 2.5만 미만 | 60 |
| 주정강화 | 2.5만 이상 5만 미만 | 85 |
| 주정강화 | 5만 이상 | 68 |

- 페어링 음식 분포
  > * 페어링 선택 시 필터링 되어 노출이 안되는 와인 타입들이 있음
  > * Fruity_desserts 선택 시 전체 와인 타입에서 58개 와인만 추려지고 Pasta 선택 시 레드 와인만 남는 경우가 발생
    
| type_id | Aperitif | Appetizers_and_snacks | Blue_cheese | Cured_Meat | Fruity_desserts | Game_ | Goat_Cheese | Lamb | Lean_fish | Mature_and_hard_cheese | Mild_and_soft_cheese | Mushrooms | Pasta | Pork | Poultry | Rich_fish | Shellfish | Spicy_food | Sweet_desserts | Veal | Vegetarian | Beef |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **레드** | **0** | **0** | 180 | 364 | **1** | 7,796 | 10 | 9,115 | **2** | 1,045 | 240 | 50 | 3,062 | 904 | 10,011 | 100 | 27 | 615 | **1** | 5,224 | 12 | 12,738 |
| **화이트** | 189 | 740 | **2** | 1,469 | 29 | 55 | 533 | **3** | 1,040 | 250 | 645 | 213 | **0** | 169 | 1,603 | 1,349 | 1,572 | 844 | 134 | **1** | 2,313 | 10 |
| **스파클링** | 359 | 338 | **0** | 242 | 18 | 80 | **1** | 41 | 207 | 56 | 346 | **2** | **0** | 105 | 232 | 558 | 415 | 25 | 8 | 12 | 280 | 59 |
| **로제** | 26 | 26 | **5** | **2** | **0** | 108 | 12 | 85 | 27 | 95 | 26 | **6** | **0** | 97 | 198 | 69 | 113 | 85 | **4** | 40 | 124 | 147 |
| **디저트** | **0** | **5** | 29 | 35 | 10 | 14 | **5** | 18 | 11 | 15 | 28 | **4** | **1** | 14 | 93 | 36 | 57 | 69 | 35 | 7 | 38 | 29 |
| **주정강화** | 35 | 55 | 29 | 35 | **0** | 6 | **0** | 8 | **0** | 139 | **1** | **0** | **0** | **4** | **5** | **2** | **1** | 8 | 11 | **0** | **0** | 118 |


### 2. DB 테이블 정보

![image](https://github.com/user-attachments/assets/6cbd9e18-f135-4ab0-b131-d6cc97d7ba02)


## 4. 웹 개발
* 사용자가 웹에서 쉽게 접근할 수 있도록 페이지를 구축
* 페이지 :  

### 1. 프론트엔드
* 페이지 적용
  > 1. 페어링 카테고리, 상세 항목 선택
  > 2. Flavor 5개까지 선택
  > 3. taste(당도, 산도, 탄닌, 강도), 바디감 선택
  > 4. 도수, 가격대 선택
  > 5. 결과보기
* 오류 및 해결
  > 1. food_child 항목 표시
  > * display.none 적용이 안되는 이슈 발생
  > * js function 이 제대로 작동되지 않아, 상위 카테고리 button 마다 addEventListener 을 적용하여 해당 상세 항목만 보이도록 설정
  > 2. 답변 선택 관련(`answer_box`, `flavor_box`)
  > * `answer_box` , `flavor_box` 내의 label 을 클릭 해야 해당 답변이 선택되는 이슈 발생
  > * label 을 감싸고 있는 box 에 `onclick="document.getElementById('id값').click();"` 추가
  > 3. 답변 선택 관련(`flavor_box`)
  > * 위의 이슈를 해결하고자 수정했으나, 오히려 `flavor_box` 의 label 제외를 클릭해야 해당 답변이 선택되는 이슈 발생
  > * `<div class="flavor_box" onclick="handleCheckboxChange(document.getElementById('id값'));">` 와 같이 수정했으나, 첫 번째 이슈로 돌아감
  > * `flavor_box` 내의 label 은 `flavor_box` 의 크기와 거의 동일하여 답변 선택에 있어서 큰 이슈가 없었기에, ii. 에서 추가했던 onclick 을 제외하기로 함
### 2. 백엔드
* 소셜로그인(구글) 연동하여 유저 정보를 저장하는 기능을 구현하려고 했으나 추천 시스템의 완성을 최우선 순위로 생각하여 로그인 기능은 제외함.
* wine_recommend API 적용
  > * 결과보기 클릭 시 유사도 적용하여 와인 5개 추천
  > * 결과 값이 없는 경우 결과 없음으로 표시하도록 적용
* 오류 및 해결
  > 1. food 와 flavor 에서 HTML 에서의 input 값과 DB의 컬럼이 같이 않아서 발생한 오류   
  > * HTML 에서 food, flavor 의 input value 값을 DB의 컬럼명과 동일하게 맞춰줌.
  > 2. `ValueError: Found array with 0 sample(s) (shape=(0, 5)) while a minimum of 1 is required by check_pairwise_arrays.` 에러 발생하며 추천 결과 아무것도 나오지 않는 문제 발생
  > * 초기에는 도수, 가격대, 종류를 필터링 요소로 넣고, 나머지 요소는 유사도 계산에 활용했음. 
  하지만 데이터 분포 상 필터링이 되면 유사도 계산을 하기도 전에 이미 추천 가능한 조합이 없어서 유사도 계산을 하지 못하여 생기는 오류였고, 다양한 추천 결과를 위해 필터링 요소에서 종류를 제외시키로 결정함.



