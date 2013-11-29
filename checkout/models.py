from django.contrib.auth.models import User
from django.db import models
from django.db.models.base import Model

from products.models import Product
from django.forms.models import ModelForm

STATE_NEW = 1
STATE_ARCHIVE = 2

class Order(Model):
    product = models.ForeignKey(Product)

    SIZE_S = 'S'
    SIZE_M = 'M'
    SIZE_L = 'L'
    SIZE_CHOICES = (
        (SIZE_S, 'S'),
        (SIZE_M, 'M'),
        (SIZE_L, 'L'),
    )
    size = models.CharField(max_length=2, choices=SIZE_CHOICES, default=SIZE_S)

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['size']

class ShoppingCart(Model):
 
    orders = models.ManyToManyField(Order)
    user = models.ForeignKey(User)
    
    ORDER_STATES = (
                    (STATE_NEW, 'New'),
                    (STATE_ARCHIVE, 'Archiv'),
                    ) 
    state = models.IntegerField(choices=ORDER_STATES, default=STATE_NEW)
    
    def close(self):
        self.state = STATE_ARCHIVE
    
    def __unicode__(self):
        state = dict(self.ORDER_STATES)[self.state]
        return "Cart of user " + str(self.user.username) + " / State: " + state
