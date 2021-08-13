from django.shortcuts import render
from .models import SellOffer
from ItemApp.models import Item
from django.db.models import Count, Min

def render_market_page(request):
    offers = (SellOffer.objects.values('item')
              .annotate(dcount=Count('item'), min_price=Min('price'))
              .order_by()
              )

    for offer in offers:
        item = Item.get_item_by_id(offer['item'])
        offer['item_name'] = item.name
        offer['item_image_url'] = item.image.url
        offer['item_rarity'] = item.rarity

    context = {
        'offers': offers
    }
    return render(request, 'market-page/market-page.html', context)
