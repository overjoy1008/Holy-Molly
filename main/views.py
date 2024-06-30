from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def login_view(request):
    return redirect('index')

def chatting_screen(request):
    return render(request, 'chatting_screen.html')  # chatting_screen.html 템플릿 렌더링
