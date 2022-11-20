from unittest import skip  # Allows skipping tests using @skip

from django.contrib.auth.models import User
from django.test import Client, RequestFactory, TestCase
from django.urls import reverse

from store.models import Category, Product
from store.views import all_products


class TestViewResponses(TestCase):
    def setUp(self):
        self.c = Client()
        self.factory = RequestFactory()
        Category.objects.create(name='White wine', slug='white-wine')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(category_id=1, title='Reisling', created_by_id=1,
                        slug='reisling', price='14.99', image='reisling')

    def test_url_allowed_hosts(self):
        # Currently ALLOWED_HOSTS = '*'
        response = self.c.get('/', HTTP_HOST = 'mydomain.com')
        self.assertEqual(response.status_code, 200)

    def test_all_products_url(self):
        response = self.c.get('/products/all-products')
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        response = self.c.get(reverse('store:product-detail', args=['reisling']))
        self.assertEqual(response.status_code, 200)

    def test_category_detail_url(self):
        response = self.c.get(reverse('store:category-detail', args=['white-wine']))
        self.assertEqual(response.status_code, 200)









