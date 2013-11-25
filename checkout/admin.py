from django.contrib import admin
from checkout.models import ShoppingCart, Order

admin.site.register(ShoppingCart)
admin.site.register(Order)