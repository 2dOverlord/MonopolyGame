from django.urls import path
from . import views

urlpatterns = [
    path('', views.render_main_page, name='main'),
    path('user/<int:user_id>/', views.render_user_page, name='user'),
    path('register/', views.render_register_page, name='register'),
    path('logout/', views.render_logout, name='logout'),
    path('login/', views.render_login_page, name='login'),
    path('sellitem/<int:item_id>', views.sell_item, name='sell_item'),
]
