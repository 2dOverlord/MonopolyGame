from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.render_main_page),
    path('', views.render_user_page, name='user')
]
