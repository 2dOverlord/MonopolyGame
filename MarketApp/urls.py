from django.urls import path
from . import views

urlpatterns = [
    path('', views.render_market_page, name='market')
]
