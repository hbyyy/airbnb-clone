from django.contrib.auth.models import AbstractUser

# Create your models here.
from django.db import models

from users.choice import GENDER_CHOICE, LANGUAGE_CHOICE, CURRENCY_CHOICES


class User(AbstractUser):
    """ Custom user model"""
    avatar = models.ImageField(blank=True, null=True)
    gender = models.CharField(choices=GENDER_CHOICE, max_length=10, blank=True)
    bio = models.TextField(blank=True)
    birthday = models.DateField(blank=True, null=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICE, max_length=2, blank=True)
    currency = models.CharField(
        choices=CURRENCY_CHOICES, max_length=3, blank=True
    )
    superhost = models.BooleanField(default=False)
