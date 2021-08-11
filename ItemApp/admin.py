from django.contrib import admin
from .models import Item, UserItemInterface

admin.site.register(Item)
admin.site.register(UserItemInterface)