from django.contrib.auth.models import User
from django.db import models

class CustomUser(User):
    friends = models.ManyToManyField("self")
    balance = models.DecimalField(decimal_places=2, null=False, max_digits=5)




