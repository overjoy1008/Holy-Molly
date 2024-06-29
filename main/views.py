from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def login_view(request):
    return redirect('index')  # 로그인 페이지로 접속하면 바로 index로 리디렉션
