from django.db import models
from django.db.models.base import Model

class ProductCategory(Model):
    name = models.CharField(max_length=20)
    
    def __unicode__(self):
        return self.name

class Product(Model):
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='prod_images/', default='no_image.gif')
    category = models.ForeignKey(ProductCategory)
    showcase = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.name

