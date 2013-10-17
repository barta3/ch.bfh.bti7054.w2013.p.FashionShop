from django.shortcuts import render
from products.models import ProductCategotry, Product
from django.core.context_processors import request

def index(request):
    cat_list = ProductCategotry.objects.all()
    context = { 'cat_list' : cat_list}
    return render(request, 'home/index.html', context)


def productListByCategory(request, cat_name):
    prod_list = Product.objects.filter(category__name=cat_name)
    cat_list = ProductCategotry.objects.all()
    context = {'prod_list' : prod_list, 'cat_list' : cat_list}
    return render(request, 'home/prodlist.html', context)