from django.db import models
from django.db.models.base import Model
from products.models import Product
from django.contrib.auth.models import User

class ShoppingCart(Model):    
    products = models.ManyToManyField(Product)
    user = models.OneToOneField(User)
    
    def __unicode__(self):
        return "Cart of user " + str(self.user.id)
