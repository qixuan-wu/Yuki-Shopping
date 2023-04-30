from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


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

    def __str__(self):
        return f'{self.rank}, {self.name}, {self.price}, {self.category}, {self.image}, {self.quantity}'


class HomeFurnishing(models.Model):
    rank = models.TextField(primary_key=True)
    name = models.TextField()
    ratings = models.TextField()
    price = models.TextField()
    image = models.TextField()
    quantity = models.TextField()

    def __str__(self):
        return f'{self.rank}, {self.name}, {self.ratings}, {self.price}, {self.image}, {self.quantity}'


class HomeFurnishingDetail(models.Model):
    rank = models.TextField()
    name = models.TextField()
    price = models.TextField()
    category = models.TextField()
    image = models.TextField()
    quantity = models.TextField()

    def __str__(self):
        return f'{self.rank}, {self.name}, {self.price}, {self.category}, {self.image}, {self.quantity}'


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=False)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_order = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
































# class cart(models.Model):
#     rank = models.IntegerField(primary_key=True)
#     name = models.FloatField()
#     price = models.TextField()
#     add_to_chart = models.BooleanField(default=False)
#     quantity = models.PositiveIntegerField(default=1)
#     def __str__(self):
#         return f'{self.rank}, {self.name}, {self.price}, {self.add_to_chart}, {self.quantity}'