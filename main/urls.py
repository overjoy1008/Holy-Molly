from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # 기본 URL에 대한 뷰 설정
    path('login/', views.login_view, name='login'),  # 로그인 URL 추가
    path('chat/', views.chatting_screen, name='chatting_screen'),  # 새로운 URL 패턴 추가
]
