from django.urls import path
from . import views

urlpatterns = [
    path('', views.render_games_page, name='games')
]
