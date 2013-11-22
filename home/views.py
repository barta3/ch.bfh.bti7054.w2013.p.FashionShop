from django.shortcuts import render
from products.models import ProductCategory, Product, ShoppingCart
from django.http.response import HttpResponseRedirect

def index(request):
    cat_list = ProductCategory.objects.all()
    cartItems = ShoppingCart.objects.filter(user=request.user.id)[0].products.all()
    
    context = { 'cat_list' : cat_list, 'cartItems' : cartItems}
    return render(request, 'home/index.html', context)


def productListByCategory(request, cat_name):
    prod_list = Product.objects.filter(category__name=cat_name)
    cat_list = ProductCategory.objects.all()
    cartItems = ShoppingCart.objects.filter(user=request.user.id)[0].products.all()
    context = {'prod_list' : prod_list, 'cat_list' : cat_list, 'cartItems' : cartItems}
    return render(request, 'home/prodlist.html', context)

def productDetail(request, cat_name, prod_id):
    cartItems = ShoppingCart.objects.filter(user=request.user.id)[0].products.all()
    context = {'prod' : Product.objects.get(id=prod_id), 'cat_list' : ProductCategory.objects.all(), 'cartItems' : cartItems}
    return render(request, 'home/productDetail.html', context)

def addToCart(request, cat_name, prod_id):
    
    print("USER " + str(request.user.id))
    
    cartByUser = ShoppingCart.objects.get_or_create(user=request.user)[0]
    
    cartByUser.products.add(Product.objects.get(id=prod_id))
    
    return HttpResponseRedirect('/home/')