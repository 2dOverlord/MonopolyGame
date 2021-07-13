from django.shortcuts import render

def render_market_page(request):
    return render(request, 'market-page/market-page.html')
