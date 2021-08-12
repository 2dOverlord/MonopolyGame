from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

from django.http import HttpResponseRedirect

from .forms import CustomRegistrationForm, CustomUserAuthenticationForm, EditProfileForm, PasswordChangingForm
from MarketApp.forms import SellForm

from .models import CustomUser
from ItemApp.models import Item

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

from django.template.loader import render_to_string
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.conf import settings

from .tokens import account_activation_token
from django.http import HttpResponse


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
            
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            username = form.cleaned_data.get('username')

            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.content_subtype = 'html'
            email.send()
            form.save()
            messages.success(request, 'Account was created for ' + username)
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

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        
        user.save()
        login(request, user)
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')