from django.contrib.auth.models import User
from django.db import models
from django.db.models.base import Model

from products.models import Product
from django.forms.models import ModelForm


class Order(Model):
    SIZE_S = 'S'
    SIZE_M = 'M'
    SIZE_L = 'L'
    SIZE_CHOICES = (
        (SIZE_S, 'S'),
        (SIZE_M, 'M'),
        (SIZE_L, 'L'),
    )
    product = models.ForeignKey(Product)
    size = models.CharField(max_length=2, choices=SIZE_CHOICES, default=SIZE_S)
    
class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['size']

class ShoppingCart(Model):    
    orders = models.ManyToManyField(Order)
    user = models.OneToOneField(User)
    
    def __unicode__(self):
        return "Cart of user " + str(self.user.username)

