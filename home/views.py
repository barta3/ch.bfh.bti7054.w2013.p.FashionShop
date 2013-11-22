from django.shortcuts import render
from products.models import ProductCategory, Product, ShoppingCart
from django.http.response import HttpResponseRedirect

def index(request):
    context = { }
    _addCategories(context)
    _addCartInfos(context, request)
        
    return render(request, 'home/index.html', context)


def productListByCategory(request, cat_name):
    prod_list = Product.objects.filter(category__name=cat_name)
#     cat_list = ProductCategory.objects.all()
    context = {'prod_list' : prod_list}
    
    _addCategories(context)
    _addCartInfos(context, request)

    return render(request, 'home/prodlist.html', context)

def productDetail(request, cat_name, prod_id):
    context = {'prod' : Product.objects.get(id=prod_id)}
    _addCategories(context)
    _addCartInfos(context, request)
    return render(request, 'home/productDetail.html', context)

def addToCart(request, cat_name, prod_id):
    
    cartByUser = ShoppingCart.objects.get_or_create(user=request.user)[0]
    
    cartByUser.products.add(Product.objects.get(id=prod_id))
    
    return HttpResponseRedirect('/home/')

def _addCartInfos(context, request):
    cart = ShoppingCart.objects.filter(user=request.user.id)
    if(cart.count() > 0):
        cartItems = ShoppingCart.objects.filter(user=request.user.id)[0].products.all()
        context['cartItems'] = cartItems
    
#     return None#

def _addCategories(context):
    cat_list = ProductCategory.objects.all()
    context['cat_list'] = cat_list

