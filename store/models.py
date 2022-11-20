from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class ProductManager(models.Manager):
    """
    Defaults product queries to filter and pull only active products.
    If you want to show products that are not active this will need disabled.
    Allows for fat models and skinny views.
    """
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(as_active=True)


class Category(models.Model):
    name = models.CharField(max_length=75, db_index=True, unique=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def get_absolute_url(self):
        return reverse('store:category-detail', args=[self.slug])


    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator')
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, blank=True)
    type = models.CharField(max_length=25, blank=True, default='Dry White')
    brand = models.CharField(max_length=255, blank=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    best_seller = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/')
    in_stock = models.BooleanField(default=True)

    """May have a product that is out of stock and incative (not for sale)
        but you dont want to delete it because you will have it in stock in the future.
        if inactive it will not display on web page
        if product.is_active display product. 
    """

    is_active = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)
    objects = models.Manager()
    products = ProductManager()

    def get_absolute_url(self):
        return reverse('store:product-detail', args=[self.slug])

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',) # Descending order

    def __str__(self):
        return self.title
    

