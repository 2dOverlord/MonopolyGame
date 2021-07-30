from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

from django.http import HttpResponseRedirect

from .forms import CustomRegistrationForm, CustomUserAuthenticationForm
from MarketApp.forms import SellForm

from .models import CustomUser
from ItemApp.models import Item


def render_main_page(request):
    return render(request, template_name='main-page/main-page.html')


def render_user_page(request, user_id=1):

    user_object = CustomUser.get_user_by_id(user_id=user_id)

    inventory = Item.get_items_by_owner(owner=user_object)
    inventory = [inventory[i:i+6] for i in range(0, len(inventory), 6)]

    form = SellForm()

    context = {
        "object": user_object,
        "inventory": list(inventory),
        "form": form,
    }

    return render(request, 'user-page/user-page.html', context)


def sell_item(request, item_id):
    if request.POST:
        form = SellForm(request.POST)

        if form.is_valid():
            item_price = form.cleaned_data['price']
            Item.put_item_on_market(item_id, item_price)
            owner_id = Item.get_owner_id_by_item_id(item_id)

    return HttpResponseRedirect(f'/user/{owner_id}')


def render_register_page(request):
    context = {}

    if request.POST:
        form = CustomRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
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


def render_login_page(request):

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
            messages.info(request, 'Username or password is incorrect')
    else:
        form = CustomUserAuthenticationForm()

    context['login_form'] = form

    return render(request, 'login-page/login-page.html', context)

