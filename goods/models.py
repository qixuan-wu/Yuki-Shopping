from django.conf import settings
from django.db import models

class HomeDcor(models.Model):
    rank = models.TextField(primary_key=True)
    name = models.TextField()
    ratings = models.TextField()
    price = models.TextField()

    def __str__(self):
        return f'{self.rank}, {self.name}, {self.ratings}, {self.price}'

class HomeFurnishing(models.Model):
    rank = models.TextField(primary_key=True)
    name = models.TextField()
    ratings = models.TextField()
    price = models.TextField()

    def __str__(self):
        return f'{self.rank}, {self.name}, {self.ratings}, {self.price}'

class HomeImprovement(models.Model):
    rank = models.TextField(primary_key=True)
    name = models.TextField()
    ratings = models.TextField()
    price = models.TextField()

    def __str__(self):
        return f'{self.rank}, {self.name}, {self.ratings}, {self.price}'
