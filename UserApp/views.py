from django.shortcuts import render
from .models import CustomUser
from ItemApp.models import Item

def render_main_page(request):
    return render(request, 'main-page/main-page.html')

def render_user_page(request, user_id = 1):
    object = CustomUser.objects.get(id=user_id)
    inventory = Item.objects.filter(owner=object)
    data = {
        "object": object,
        "inventory": list(inventory),
    }
    return render(request, 'user-page/user-page.html', data)