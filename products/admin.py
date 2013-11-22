from django.contrib import admin
from products.models import Product, ProductCategory, ShoppingCart

admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(ShoppingCart)