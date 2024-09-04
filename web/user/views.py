from pathlib import Path
import os, json
from django.shortcuts import redirect,HttpResponseRedirect
from .models import User
from django.http import JsonResponse
import requests
from rest_framework import status, serializers
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

#-- .env 적용
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(os.path.join(BASE_DIR, '.env'))

GOOGLE_SCOPE_USERINFO = os.getenv("GOOGLE_SCOPE_USERINFO")
GOOGLE_REDIRECT = os.getenv("GOOGLE_REDIRECT")
GOOGLE_CALLBACK_URI = os.getenv("GOOGLE_CALLBACK_URI")
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_SECRET = os.getenv("GOOGLE_SECRET")
STATE = os.getenv("STATE")
#---

# 구글 소셜로그인 URL 설정

BASE_URL = 'http://localhost:8000'

# 로그인 함수
def google_login(request):
    scope = "https://www.googleapis.com/auth/userinfo.email profile"
    client_id = GOOGLE_CLIENT_ID
    redirect_uri = GOOGLE_CALLBACK_URI  
    return redirect(f"https://accounts.google.com/o/oauth2/v2/auth?client_id={client_id}&response_type=code&redirect_uri={redirect_uri}&scope={scope}")

# 콜백 함수
def google_callback(request):
    client_id = GOOGLE_CLIENT_ID
    client_secret = GOOGLE_SECRET
    redirect_uri = GOOGLE_CALLBACK_URI 
    code = request.GET.get('code')
    
    # 구글로부터 액세스 토큰을 요청
    token_req = requests.post(
        "https://oauth2.googleapis.com/token",
        data={
            'client_id': client_id,
            'client_secret': client_secret,
            'code': code,
            'grant_type': 'authorization_code',
            'redirect_uri':redirect_uri 
        }
    )
    
    token_req_json = token_req.json()
    error = token_req_json.get("error")
    
    if error:
        return JsonResponse({'status': 400, 'message': 'token Error'}, status=400)
    
    google_access_token = token_req_json.get('access_token')
    
    # 구글 사용자 정보 요청
    user_info_response = requests.get(
        "https://www.googleapis.com/oauth2/v1/userinfo",
        params={'access_token': google_access_token}
    )
    
    if user_info_response.status_code != 200:
        return JsonResponse({'status': 400, 'message': 'Failed to fetch user info'}, status=400)
    
    user_info = user_info_response.json()
    email = user_info.get('email')
    name = user_info.get('name')
    
    if not email:
        return JsonResponse({'status': 400, 'message': 'No email found'}, status=400)
    
    # 사용자 생성 또는 가져오기
    user, created = User.objects.get_or_create(email=email, defaults={'username': name})
    
    # JWT 토큰 생성
    refresh = RefreshToken.for_user(user)
    
    response_data = {
        'access_token': str(refresh.access_token),
        'refresh_token': str(refresh),
        'message': 'Login successful' if not created else 'User created and logged in'
    }
    
    # 로그인 성공 후 루트 경로로 리디렉션
    return HttpResponseRedirect(BASE_URL)
  