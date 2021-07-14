from django.urls import path
from . import views

urlpatterns = [
    path('', views.render_main_page),
    path('user/<int:user_id>/', views.render_user_page, name='user')
]
