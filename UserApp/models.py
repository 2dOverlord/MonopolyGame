from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True)
    is_active = models.BooleanField(default=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(verbose_name="email", unique=True, max_length=60)
    image = models.ImageField(blank=True, null=True)
    friends = models.ManyToManyField("self", blank=True, null=True)
    balance = models.DecimalField(decimal_places=2, null=True, blank=True, max_digits=5, default=00.00)

    USERNAME_FIELD = 'email'


