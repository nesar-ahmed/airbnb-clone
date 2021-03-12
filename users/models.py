from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    GENDER_CHOICES = (("male", "Male"), ("female", "Female"), ("other", "Other"))
    LANGUAGE_CHOICES = (
        ("portuguese", "Portuguese"),
        ("english", "English"),
        ("bengali", "Bengali"),
    )
    CURRENCY_CHOICES = (("euro", "Euro"), ("USD", "USD"), ("bdt", "BDT"))
    avatar = models.ImageField(null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=15, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=15, blank=True)
    bio = models.TextField(blank=True)
    superhost = models.BooleanField(default=False)

    def __str__(self):
        return self.username
