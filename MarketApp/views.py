from django.shortcuts import render
from ItemApp.models import Item

def render_market_page(request):
    items = Item.get_all_on_sale_items()
    context = {
        'items': items
    }
    return render(request, 'market-page/market-page.html', context)
