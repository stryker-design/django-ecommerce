from django.test import TestCase
from django.contrib.auth.models import User

from store.models import Category, Product


class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name='White wine', slug='white-wine')

    def test_category_model_entry(self):
        """
            Test Category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))
        self.assertEqual(str(data), 'White wine')


class TestProductsModel(TestCase):
    def setUp(self):
        Category.objects.create(name='White wine', slug='white-wine')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(category_id=1, title='Reisling', created_by_id=1,
                        slug='reisling', price='14.99', image='reisling')

        
    def test_products_model_entry(self):
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'Reisling')

