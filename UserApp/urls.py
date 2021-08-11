from django.urls import path
from . import views
from .views import UserEditView, PasswordsChangeView
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
]
