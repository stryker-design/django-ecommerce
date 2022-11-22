from django.db import models

from django.contrib.auth.models import User
from store.models import Product
from django.conf import settings


# Create your models here.

# class Customer(models.Model):
#     user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
#     name = models.CharField(max_length=200, null=True)
#     email = models.EmailField()

# class Order(models.Model):
#     customer = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
#     date_ordered = models.DateTimeField(auto_now_add=True)
#     complete = models.BooleanField(default=False)
#     transaction_id = models.CharField(max_length=100, null=True)

#     @property
#     def get_cart_total(self):
#         orderitems = self.orderitem_set.all()
#         total = sum([item.get_total for item in orderitems])
#         return total

#     @property
#     def get_cart_items(self):
#         orderitems = self.orderitem_set.all()
#         total = sum([item.qunatity for item in orderitems])
#         return total 

#     def __str__(self):
# 	    return str(self.id) + str(self.customer)



# class OrderItems(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
#     order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
#     quantity = models.IntegerField(default=0, null=True, blank=True)
#     date_added = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         verbose_name_plural = 'Order items'

#     @property
#     def get_total(self):
#         total = self.product.price * self.quantity
#         return total



# class ShippingAddress(models.Model):
# 	customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
# 	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
# 	address = models.CharField(max_length=200, null=False)
# 	city = models.CharField(max_length=200, null=False)
# 	state = models.CharField(max_length=200, null=False)
# 	zipcode = models.CharField(max_length=200, null=False)
# 	date_added = models.DateTimeField(auto_now_add=True)

# 	def __str__(self):
# 		return self.address