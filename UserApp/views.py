from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

from .models import CustomUser
from ItemApp.models import Item

from .forms import CustomRegistrationForm, CustomUserAuthenticationForm


def render_main_page(request):
    return render(request, template_name='main-page/main-page.html')


def render_user_page(request, user_id=1):

    user_object = CustomUser.get_user_by_id(user_id=user_id)
    inventory = Item.get_items_by_owner(owner=user_object)

    context = {
        "object": user_object,
        "inventory": list(inventory),
    }

    return render(request, 'user-page/user-page.html', context)


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


def render_logout(request):
    logout(request)
    return redirect('main')


def render_login(request):

    context = {}
    user = request.user

    if user.is_authenticated:
        return redirect('main')

    if request.POST:
        form = CustomUserAuthenticationForm(request.POST)

        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)

                return redirect('main')
    else:
        form = CustomUserAuthenticationForm()

    context['login_form'] = form

    return render(request, 'login-page/login-page.html', context)

