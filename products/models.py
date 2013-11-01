from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(max_length=20)
    
    def __unicode__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=20)
    desc = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ForeignKey(ProductCategory)
    
    def __unicode__(self):
        return self.name