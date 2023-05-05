from django.test import TestCase, Client
from django.urls import reverse
from goods.models import HomeDcor, HomeDecorDetail, cart
from .views import (display_HomeDcor, display_HomeDcorDetail, add_to_cart, remove_from_cart, home_list)
from django.contrib.auth.models import User


class ShopModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # set up test data in database
        HomeDcor.objects.create(rank='1', name='product1', ratings='5', price='10.00', image='image1', quantity='10')
        HomeDcor.objects.create(rank='2', name='product2', ratings='4', price='15.00', image='image2', quantity='20')
        HomeDecorDetail.objects.create(rank='1', name='product1', price='10.00', category='category1', image='image1', quantity='10', latitude=1.0, longitude=2.0)
        HomeDecorDetail.objects.create(rank='2', name='product2', price='15.00', category='category2', image='image2', quantity='20', latitude=3.0, longitude=4.0)
        cart.objects.create(id=1, name='product1', quantity=2, price=10.00, add_to_cart=True)
        cart.objects.create(id=2, name='product2', quantity=1, price=15.00, add_to_cart=False)

    def test_HomeDcor_model(self):
        product1 = HomeDcor.objects.get(rank='1')
        product2 = HomeDcor.objects.get(rank='2')
        self.assertEqual(product1.name, 'product1')
        self.assertEqual(product2.quantity, '20')
    
    def test_HomeDecorDetail_model(self):
        product1 = HomeDecorDetail.objects.get(rank='1')
        product2 = HomeDecorDetail.objects.get(rank='2')
        self.assertEqual(product1.category, 'category1')
        self.assertEqual(product2.latitude, 3.0)

    def test_cart_str(self):
        # test the string representation of a cart object
        cart_item = cart.objects.get(id=1)
        expected_str = "1, product1, 2, 10.00"
        self.assertEqual(str(cart_item), expected_str)


    def test_cart_add_to_cart(self):
        # test the add_to_cart field of a cart object
        cart_item = cart.objects.get(id=1)
        self.assertTrue(cart_item.add_to_cart)

class HomeDecorViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.home_decor1 = HomeDcor.objects.create(rank=1, name='Decor1')
        self.home_decor2 = HomeDcor.objects.create(rank=2, name='Decor2')
        self.url = reverse('display_HomeDcor')

    def test_display_HomeDcor_with_no_query_params(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.home_decor1.name)
        self.assertContains(response, self.home_decor2.name)

    def test_display_HomeDcor_with_query_param(self):
        response = self.client.get(self.url, {'query': 'Decor1'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.home_decor1.name)
        self.assertNotContains(response, self.home_decor2.name)
