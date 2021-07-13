from django.db import models
from UserApp.models import CustomUser

ITEM_TYPES = (
    [1, 'ONE'],
    [2, 'TWO']
)

RARITIES = [
    [0, 'RARE'],
    [1, 'NOT RARE']
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
    price = models.DecimalField(decimal_places=2, null=True, max_digits=5)