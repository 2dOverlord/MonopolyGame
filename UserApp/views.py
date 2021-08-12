from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

from django.http import HttpResponseRedirect

from .forms import CustomRegistrationForm, CustomUserAuthenticationForm, EditProfileForm, PasswordChangingForm
from MarketApp.forms import SellForm

from .models import CustomUser
from ItemApp.models import UserItemInterface
from MarketApp.models import SellOffer

from itertools import chain

from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView

from django.core.mail import EmailMessage
from django.views import View
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .utils import token_generator

def render_main_page(request):
    return render(request, template_name='main-page/main-page.html')


def render_user_page(request, user_id=1):

    user_object = CustomUser.get_user_by_id(user_id=user_id)

    inventory = UserItemInterface.get_items_by_user(user=user_object)
    ids = [obj.id for obj in inventory]
    inventory = [[obj] * obj.quantity for obj in inventory]
    inventory = list(chain(*inventory))
    inventory = [inventory[i:i + 6] for i in range(0, len(inventory), 6)]

    form = SellForm()

    context = {
        "object": user_object,
        "inventory": list(inventory),
        "ids": ids,
        "form": form,
    }

    return render(request, 'user-page/user-page.html', context)


def sell_item(request, item_id):
    if request.POST:
        form = SellForm(request.POST)

        if form.is_valid():
            item_price = form.cleaned_data['price']
            obj = SellOffer.make_offer(price=item_price, interface_id=item_id)
            user_id = obj.user.id

    return HttpResponseRedirect(f'/user/{user_id}')


def render_register_page(request):
    context = {}

    if request.POST:
        form = CustomRegistrationForm(request.POST)

        if form.is_valid():
            user = form.cleaned_data.get('username')
            email = request.POST['email']
            form.email_verified = False
            form.save()
            email_subject = 'Activate your account'

            # path to view
            uidb64 = urlsafe_base64_encode(force_bytes(form.pk))

            domain = get_current_site(request).domain
            link = reverse('activate', kwargs={'uidb64': uidb64, 'token': token_generator.make_token(form)})
            activate_url = 'http://' + domain + link

            email_body = 'Hi ' + user + 'Please use this link to verify your account \n' + activate_url
            email = EmailMessage(
                email_subject,
                email_body,
                'noreply@gmail.com',
                [email],
            )
            email.send(fail_silently=False)
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
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)

                return redirect('main')
        else:
            messages.info(request, 'Username or password is incorrect')
    else:
        form = CustomUserAuthenticationForm()

    context['login_form'] = form

    return render(request, 'login-page/login-page.html', context)


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'edit-page/edit.html'
    success_url = reverse_lazy('main')

    def  get_object(self):
        return self.request.user


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('main')


class VerificationView(View):
    def get(self, request, uidb64, token):

            id = force_text(urlsafe_base64_decode(uidb64))  # Probles somewhere here
            user = CustomUser.objects.get(pk=id)

            if user.email_verified:
                return redirect('login')
            user.email_verified = True
            user.save()

            messages.success(request, 'Account activated successfully')
            return redirect('login')