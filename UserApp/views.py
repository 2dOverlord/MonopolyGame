from django.shortcuts import render, redirect
from .models import CustomUser
from ItemApp.models import Item
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .forms import CustomRegistrationForm

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

def render_register_page(request):
    context = {}
    if request.POST:
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            print('NOT VALID')
            context['registration_form'] = form
    else:
        form = CustomRegistrationForm()
        context['registration_form'] = form
    return render(request, 'register-page/register-page.html', context)