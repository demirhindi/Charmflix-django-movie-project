
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db.models.signals import pre_save
from django.utils.text import slugify
from movies.models import Film
from series.models import Serie
from django.conf import settings
import stripe

from series.models import Serie


class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    
    avatar = models.ImageField(default='default.png', upload_to='avatar')
    stripe_customer_id= models.CharField(blank=True,null=True,max_length=100)
    favorites = models.ManyToManyField(Film, blank=True, related_name="watchfilms")
    favoritesseries = models.ManyToManyField(Serie, blank=True, related_name="watchseries")

    class Meta:
        verbose_name='customer'
        verbose_name_plural='customers'

    def __str__(self):
        return self.user.username

    
        
