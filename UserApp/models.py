from django.contrib.auth.models import User
from django.db import models


class CustomUser(User):
    image = models.ImageField(blank=True, null=True)
    friends = models.ManyToManyField("self", blank=True, null=True)
    balance = models.DecimalField(decimal_places=2, null=False, max_digits=5)




