from django.urls import path
from . import views
from .views import UserEditView, PasswordsChangeView, VerificationView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.render_main_page, name='main'),
    path('user/<int:user_id>/', views.render_user_page, name='user'),
    path('register/', views.render_register_page, name='register'),
    path('logout/', views.render_logout, name='logout'),
    path('login/', views.render_login_page, name='login'),
    path('sellitem/<int:item_id>', views.sell_item, name='sell_item'),
    path('edit/', UserEditView.as_view(), name='edit'),
    path('password/', PasswordsChangeView.as_view(template_name='change-password/change_password.html'), name = 'password'),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='password-reset/password_reset.html'), name = "reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='password-reset-sent/password_reset_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password-reset-form/password_reset_form.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password-reset-complete/password_reset_complete.html'), name='password_reset_complete'),

    path('activate/<uidb64>/<token>', views.activate, name='activate'),
]
