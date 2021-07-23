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
    item_name = models.CharField(null=False, max_length=30)
    item_type = models.CharField(
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