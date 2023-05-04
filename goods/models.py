from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings





class HomeDcor(models.Model):
    rank = models.TextField(primary_key=True)
    name = models.TextField()
    ratings = models.TextField()
    price = models.TextField()
    image = models.TextField()
    quantity = models.TextField()

    def __str__(self):
        return f'{self.rank}, {self.name}, {self.ratings}, {self.price}, {self.image}, {self.quantity}'


class HomeDecorDetail(models.Model): 
    rank = models.TextField()
    name = models.TextField()
    price = models.TextField()
    category = models.TextField()
    image = models.TextField()
    quantity = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f'{self.rank}, {self.name}, {self.price}, {self.category}, {self.image}, {self.quantity},{self.latitude},{self.longitude}'




class cart(models.Model):
    id=models.IntegerField(primary_key=True)
    name = models.TextField()
    quantity = models.IntegerField(default=False)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    add_to_cart = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id}, {self.name}, {self.quantity}, {self.price}'

    def total_price(self):
        return sum(item.quantity * item.name.price for item in self.cart_items.all())



