from django.http import JsonResponse
from django.shortcuts import render
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import StandardScaler
from scipy.sparse import hstack
import sqlalchemy
from urllib import parse
from urllib.parse import quote_plus
from django.views.decorators.csrf import csrf_exempt
import os
from pathlib import Path
from dotenv import load_dotenv

#유클리안 유사도에 필요
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.preprocessing import MinMaxScaler


# 와인 데이터 불러오기
load_dotenv("../.env")

user = os.getenv("DB_USER")
host = os.getenv("DB_HOST")
database = os.getenv("DB_NAME")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
database = os.getenv("DB_NAME")

engine = sqlalchemy.create_engine(f"mysql://{user}:{password}@{host}:{port}/{database}")


df = pd.read_sql_query("select * from merge_items", engine)
#--

# 수치형 값을 범위로 변환하는 함수
def body_range(body_value):
    if 0 <= body_value < 2:
        return 1
    elif 2 <= body_value < 4:
        return 2
    elif 4 <= body_value < 6:
        return 3
    else:
        return 4

def acidity_range(acidity_y_value):
    if 0 <= acidity_y_value < 2:
        return 1
    elif 2 <= acidity_y_value < 4:
        return 2
    elif 4 <= acidity_y_value < 6:
        return 3
    else:
        return 4 
        
    
def tannin_range(tannin_value):
    if 0 <= tannin_value < 2:
        return 1
    elif 2 <= tannin_value < 4:
        return 2
    elif 4 <= tannin_value < 6:
        return 3
    else:
        return 4 
       
def itensity_range(intensity_value):
    if 0 <= intensity_value < 2:
        return 1
    elif 2 <= intensity_value < 4:
        return 2
    elif 4 <= intensity_value < 6:
        return 3
    else:
        return 4        
         
def sweetness_range(sweetness_value):
    if 0 <= sweetness_value < 2:
        return 1
    elif 2 <= sweetness_value < 4:
        return 2
    else:
        return 3
  

# 와인 추천을 위한 뷰
#@csrf_exempt
def recom(request):
    
    if request.method == "POST":
        
        try:
            
            
          
            # 맛   
            user_preferences = {            
                'body': int(request.POST.get('body')),
                'acidity_y': int(request.POST.get('acidity')),
                'tannin': int(request.POST.get('tannin')),
                'intensity': int(request.POST.get('intensity')),
                'sweetness': int(request.POST.get('sweetness')), 
            }

            user_data = pd.DataFrame([user_preferences])

            # alcohol & price
            alcohol_choice = int(request.POST.get('alcohol'))

            if alcohol_choice == 1:
                alcohol_min, alcohol_max = 0, 12.5
            elif alcohol_choice == 2:
                alcohol_min, alcohol_max = 12.5, 14
            elif alcohol_choice == 3:
                alcohol_min, alcohol_max = 14, 16
            elif alcohol_choice == 4: 
                alcohol_min, alcohol_max = 16, 100

            price_choice = int(request.POST.get('price'))
    
            if price_choice == 1:
                min_price, max_price = 0, 15000
            elif price_choice == 2:
                min_price, max_price = 15000, 25000
            elif price_choice == 3:
                min_price, max_price = 25000, 35000
            elif price_choice == 4:
                min_price, max_price = 35000, 60000
            elif price_choice ==5: 
                min_price, max_price = 60000, 1000000000


            filtered_wines = df[
            (df['alcohol'] >= alcohol_min) &
            (df['alcohol'] < alcohol_max)&
            (df['Price'] >= min_price) &
            (df['Price'] < max_price)
            ]   

            # type
            #preferred_type = int(request.POST.get('type'))
            #filtered_wines = filtered_wines[filtered_wines['type_id'] == preferred_type]


            # flavor
            selected_flavors = request.POST.getlist('flavor') 

            valid_flavors = [flavor for flavor in selected_flavors if flavor and flavor in df.columns]


            # food
            selected_food = request.POST.get('food')      
            filtered_wines = filtered_wines[filtered_wines[selected_food] == 1]

            #수치데이터를 범위에 맞는 데이터로 칼럼 생성
            filtered_wines['body_range'] = filtered_wines['body'].apply(body_range)
            filtered_wines['acidity_range'] = filtered_wines['acidity_y'].apply(acidity_range)
            filtered_wines['tannin_range'] = filtered_wines['tannin'].apply(tannin_range)
            filtered_wines['intensity_range'] = filtered_wines['intensity'].apply(itensity_range)
            filtered_wines['sweetness_range'] = filtered_wines['sweetness'].apply(sweetness_range)


            wine_features = filtered_wines[['body_range', 'acidity_range', 'tannin_range', 'intensity_range', 'sweetness_range']]


            distances = euclidean_distances(wine_features, user_data)



            scaler = MinMaxScaler()
            flavor_weight = 0.1 
            food_weight = 0.1

            if valid_flavors:


                filtered_wines[valid_flavors] = scaler.fit_transform(filtered_wines[valid_flavors])
                flavor_scores = filtered_wines[valid_flavors].sum(axis=1) * flavor_weight
            else:
                flavor_scores = 0 # flavor 아무것도 선택하지 않았을경우 flavor_score = 0 , flavor 로 필터링은 안함.

            if selected_food in filtered_wines.columns:
                food_scores = filtered_wines[selected_food].fillna(0) * food_weight
            else:
                food_scores = 0



            filtered_wines['similarity_score'] = distances.flatten() - flavor_scores - food_scores


            # 추천 결과 추출
            def recommend_similar_wines_to_user(filtered_wines, df, n=5):
                top_wines = filtered_wines.sort_values(by='similarity_score').head(5)
                
                top_wines['type_id_kor'] = df['type_id'].replace({1: '레드와인', 2: '화이트와인', 3: '스파클링와인', 4: '로제와인', 7: '디저트와인', 24: '주정강화와인'})

                recommendations = []
                for idx, row in top_wines.iterrows():
                    wine_info = {
                        'index': idx,
                        'name': row['name'],
                        'rating_average': row['rating_average'],
                        'rating_count' : f"{row['rating_count']:,}",
                        'alcohol': row['alcohol'],
                        'similarity_score': row['similarity_score'],
                        'price': f"{row['Price']:,}",
                        'brand_name': row['brand_name'],
                        'img': row['img_url'],
                        'url': f"http://www.vivino.com/w/{row['wine_id']}",
                        'type': row['type_id_kor'],


                    }
                    recommendations.append(wine_info)
                return recommendations

            # 추천된 와인의 정보를 리스트로 생성
            similar_wines = recommend_similar_wines_to_user(filtered_wines, df, n=5)



            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'recommendations': similar_wines})
            else:
                return render(request, 'recom/wine_recommend.html', {'recommendations': similar_wines})
        
        except ValueError as e:
            return JsonResponse({'error': str(e)})
        

    
    return render(request, 'recom/wine_recommend.html')