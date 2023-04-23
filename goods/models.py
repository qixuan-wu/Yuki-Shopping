from django.conf import settings
from django.db import models

class HomeDcor(models.Model):
    rank = models.TextField(primary_key=True)
    name = models.TextField()
    ratings = models.TextField()
    price = models.TextField()

    def __str__(self):
        return f'{self.rank}, {self.name}, {self.ratings}, {self.price}'

class HomeDecorDetail(models.Model): 
    name = models.TextField()
    price = models.TextField()
    category = models.TextField()
    image = models.TextField()

    def __str__(self):
        return f'{self.name}, {self.price}, {self.category}, {self.image}'

class HomeFurnishing(models.Model):
    rank = models.TextField(primary_key=True)
    name = models.TextField()
    ratings = models.TextField()
    price = models.TextField()

    def __str__(self):
        return f'{self.rank}, {self.name}, {self.ratings}, {self.price}'

class HomeFurnishingDetail(models.Model):
    name = models.TextField()
    price = models.TextField()
    category = models.TextField()
    image = models.TextField()

    def __str__(self):
        return f'{self.name}, {self.price}, {self.category}, {self.image}'
