from django.shortcuts import render

def render_main_page(request):
    return render(request, 'main-page/main-page.html')

def render_user_page(request):
    return render(request, 'user-page/user-page.html')