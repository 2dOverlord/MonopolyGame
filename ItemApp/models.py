from django.db import models
from django.db.models import Count
from django.db.models import Min

from UserApp.models import CustomUser

ITEM_TYPES = (
    ["Player", 'PLAYER'],
    ["Manager", 'MANAGER'],
    ["Team", 'TEAM']
)

RARITIES = [
    ["0", 'BASIC'],
    ['1', 'RARE'],
    ['2', 'LEGEND']
]


class Item(models.Model):
    name = models.CharField(null=False, max_length=30)

    type = models.CharField(
        choices=ITEM_TYPES,
        default='ONE',
        max_length=30,
    )

    rarity = models.CharField(
        choices=RARITIES,
        default='NOT RARE',
        max_length=30,
    )

    image = models.ImageField(null=True, blank=True, upload_to='images/')

    def get_values(self):
        data = {
            'name': self.name,
            'type': self.type,
            'rarity': self.rarity,
            'image_url': self.image.url
        }
        return data

    @classmethod
    def get_item_by_id(cls, item_id=1):
        return cls.objects.get(id=item_id)

    @classmethod
    def put_item_on_market(cls, item_id, item_price):
        item = cls.objects.get(id=item_id)

        item.on_sale = True
        item.price = item_price
        item.save()

        return True

    @classmethod
    def get_owner_id_by_item_id(cls, item_id):
        item = cls.objects.get(id=item_id)
        owner_id = item.owner.get_id()

        return owner_id

    @classmethod
    def get_all_on_sale_items(cls):
        items = cls.objects.filter(on_sale=True).aggregate(price=Min('price'))

        return items


class UserItemInterface(models.Model):
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField(default=1)

    @classmethod
    def get_items_by_user(cls, user):
        objects = cls.objects.filter(user=user)

        return objects
