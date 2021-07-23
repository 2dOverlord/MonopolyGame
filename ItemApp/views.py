from django.shortcuts import render
from .models import Item

# Create your views here.

def render_item_page(request, item_id=1):

    item_object = Item.get_item_by_id(item_id)

    context = {
        'object': item_object
    }

    return render(request, 'item-page/item-page.html', context)