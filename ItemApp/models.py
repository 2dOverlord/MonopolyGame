from django.db import models

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

    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    on_sale = models.BooleanField(default=False, null=False)
    price = models.DecimalField(decimal_places=2, null=True, blank=True, max_digits=5)

    image = models.ImageField(null=True, blank=True, upload_to='images/')

    @classmethod
    def get_items_by_owner(cls, owner):
        return cls.objects.filter(owner=owner)

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
