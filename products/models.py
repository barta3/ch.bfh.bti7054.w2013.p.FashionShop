from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User

class ProductCategory(Model):
    name = models.CharField(max_length=20)
    
    def __unicode__(self):
        return self.name

class Product(Model):
    name = models.CharField(max_length=20)
    desc = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='prod_images/', default='no_image.gif')
    category = models.ForeignKey(ProductCategory)
    
    def __unicode__(self):
        return self.name
    
class ShoppingCart(Model):    
    products = models.ManyToManyField(Product)
    user = models.OneToOneField(User)
    
    def __unicode__(self):
        return "Cart of user " + str(self.user.id)
