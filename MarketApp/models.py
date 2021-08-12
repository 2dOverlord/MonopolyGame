from django.db import models

from UserApp.models import CustomUser
from ItemApp.models import Item, UserItemInterface


class SellOffer(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    price = models.DecimalField(blank=False, null=False, decimal_places=2, max_digits=20)

    @classmethod
    def make_offer(cls, price, interface_id):
        interface = UserItemInterface.get_interface_by_id(interface_id)
        interface.quantity -= 1

        item = interface.item
        user = interface.user

        interface.save()

        offer = cls(item=item, user=user, price=price)
        offer.save()

        return offer
