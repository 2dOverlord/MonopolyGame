from django.shortcuts import render
from .models import SellOffer

def render_market_page(request):
    offers = SellOffer.objects.all()
    context = {
        'offers': offers
    }
    return render(request, 'market-page/market-page.html', context)
