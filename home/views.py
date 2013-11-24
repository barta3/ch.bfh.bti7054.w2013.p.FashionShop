from django.shortcuts import render
from products.models import ProductCategory, Product
from django.http.response import HttpResponseRedirect
from checkout.views import _addCartInfos
from checkout.models import ShoppingCart

def index(request):
    context = { }
    addCategories(context)
    _addCartInfos(context, request)
        
    return render(request, 'home/index.html', context)


def productListByCategory(request, cat_name):
    prod_list = Product.objects.filter(category__name=cat_name)
#     cat_list = ProductCategory.objects.all()
    context = {'prod_list' : prod_list}
    
    addCategories(context)
    _addCartInfos(context, request)

    return render(request, 'home/prodlist.html', context)

def productDetail(request, cat_name, prod_id):
    context = {'prod' : Product.objects.get(id=prod_id)}
    addCategories(context)
    _addCartInfos(context, request)
    return render(request, 'home/productDetail.html', context)

def addToCart(request, cat_name, prod_id):
    
    cartByUser = ShoppingCart.objects.get_or_create(user=request.user)[0]
    
    cartByUser.products.add(Product.objects.get(id=prod_id))
    
    return HttpResponseRedirect('/home/')
    

def addCategories(context):
    cat_list = ProductCategory.objects.all()
    context['cat_list'] = cat_list

